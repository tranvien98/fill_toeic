import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM

use_cuda = torch.cuda.is_available()
print(use_cuda)
device = torch.device("cuda" if use_cuda else "cpu")

bertmodel = 'bert-base-uncased'
tokenizer = BertTokenizer.from_pretrained(bertmodel)

model = BertForMaskedLM.from_pretrained(bertmodel).to(device)
model.eval()
import json
with open('data.json') as input_json:
    data = json.load(input_json)
def get_score(question_tensors, segment_tensors, masked_index, candidate):

    candidate_tokens = tokenizer.tokenize(candidate) # warranty -> ['warrant', '##y']
    # print(candidate_tokens)
    candidate_ids = tokenizer.convert_tokens_to_ids(candidate_tokens)
    # print(candidate_ids)
    predictions = model(question_tensors, segment_tensors)
    # print(0, masked_index, candidate_ids)
    predictions_candidates = predictions[0, masked_index, candidate_ids].mean()
    # print(predictions_candidates)

    return predictions_candidates.item()
correct = 0
false_anwser = {}
for (k, row) in data.items():
    question_tokens = tokenizer.tokenize(row['question'].replace('___', '_'))
    # print(question_tokens)
    masked_index = question_tokens.index('_')
    question_tokens[masked_index] = '[MASK]'
    segment_ids = [0] * len(question_tokens)
    segment_tensors = torch.tensor([segment_ids]).to(device)
    question_ids = tokenizer.convert_tokens_to_ids(question_tokens)
    question_tensors = torch.tensor([question_ids]).to(device)
    # print(segment_tensors)
    candidates = [row['1'], row['2'], row['3'], row['4']]
    predict_tensor = torch.tensor([get_score(question_tensors, segment_tensors,
                                    masked_index , candidate) for candidate in candidates])
    # print(predict_tensor)
    predict_idx = torch.argmax(predict_tensor).item()
    # print(candidates[predict_idx])
    if candidates[predict_idx] == row['anwser']:
        correct += 1
        # print(correct, k)
    else:
        false_anwser[k] = row
with open('false_aneser', 'w') as output_json:
    json.dump(false_anwser, output_json)
print(correct)