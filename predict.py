import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM


class FillBert():
    def __init__(self):
        self.use_cuda = torch.cuda.is_available()
        self.device = torch.device("cuda" if self.use_cuda else "cpu")
        self.bertmodel = 'bert-large-uncased'
        self.tokenizer = BertTokenizer.from_pretrained(self.bertmodel)
        self.model = BertForMaskedLM.from_pretrained(self.bertmodel).to(self.device)
        self.model.eval()
    def get_score(self,question_tensors, segment_tensors, masked_index, candidate):
        candidate_tokens = self.tokenizer.tokenize(candidate)  # warranty -> ['warrant', '##y']
        candidate_ids = self.tokenizer.convert_tokens_to_ids(candidate_tokens)
        predictions = self.model(question_tensors, segment_tensors)
        predictions_candidates = predictions[0,masked_index, candidate_ids].mean()
        return predictions_candidates.item()
    def predict(self,row):
        question_tokens = self.tokenizer.tokenize(row['question'].replace('___', '_'))
        masked_index = question_tokens.index('_')
        question_tokens[masked_index] = '[MASK]'
        segment_ids = [0] * len(question_tokens)
        segment_tensors = torch.tensor([segment_ids]).to(self.device)
        question_ids = self.tokenizer.convert_tokens_to_ids(question_tokens)
        question_tensors = torch.tensor([question_ids]).to(self.device)
        candidates = [row['1'], row['2'], row['3'], row['4']]
        predict_tensor = torch.tensor([self.get_score(question_tensors, segment_tensors,
                                                masked_index, candidate) for candidate in candidates])
        predict_idx = torch.argmax(predict_tensor).item()
        return candidates[predict_idx]
