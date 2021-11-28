from pds.database.document import Document
from pds.database.connection import Connection
from pds.candidate_retrieval.pre_processing import WordPreprocessing
from pds.pre_processing.vnm_preprocessing import VnmPreprocessing
from pds.reader.input import readInput
from pds.candidate_retrieval.candidate import CandidateList
from pds.candidate_retrieval.similarity_metric import SimilarityMetric
from pds.exhaustive.sentence import EngSentence, VieSentence
from pds.exhaustive.string_based import StringBasedTechnique
from pds.exhaustive.result import Evidence, Result


database = Connection(
    'mongodb://127.0.0.1:27017/', 'Documents').getDatabase()

# vie_offline_string_based_with_rabinkarp(
# database, 'vie', 'inputs', 3, SimilarityMetric.Jaccard_1(), 5, 101)
<<<<<<< HEAD
input_vie = readInput(input_path)
=======
input_vie = readInput('inputs')
>>>>>>> 9fb4ce608c92002bb74492b37036502364db2539
SM_list = []
for i in range(81):
    SM_list.append(0.0)

<<<<<<< HEAD
collection = Document.getCollection(database, 'vie')
candidate_list = CandidateList(
    SM_list, collection).get_k_top_similarity(3)
=======
col = Document.getCollection(database, 'vie')
candidate_list = CandidateList(
    SM_list, col).get_k_top_similarity(3)
>>>>>>> 9fb4ce608c92002bb74492b37036502364db2539

print('Candidate Retrieval done!')
# Step 3: Exhaustive Comparison

result = Result(input_vie.getTitle())
<<<<<<< HEAD
for candidate in candidate_list:
    print(candidate.getTitle())
print(Document.getDocument(database, 'vie', {'Title': str(
    candidate_list[0].getTitle()), 'Content': 1})[0]['Content'])
candidate_list_full = list(map(lambda candidate: Document.getDocument(
    database, collection, {'Title': candidate.getTitle(), 'Content': 1}), candidate_list))
=======
candidate_list_full = list(map(lambda candidate: Document.getDocument(
    database, 'vie', {'Title': candidate.getTitle(), 'Content': 1}), candidate_list))

>>>>>>> 9fb4ce608c92002bb74492b37036502364db2539
input_sent_list = VnmPreprocessing.sentence_split(
    input_vie.getContent())
input_sent_list_with_word = list(
    map(lambda sent: VieSentence(sent), input_sent_list))

for candidate in candidate_list_full:
    candidate_sent_list = VnmPreprocessing.sentence_split(
<<<<<<< HEAD
        candidate['Content'])
    candidate_sent_list_with_word = list(
        map(lambda sent: VieSentence(sent), candidate_sent_list))
    evidence = Evidence(candidate['Title'], StringBasedTechnique.n_gram_matching(
        input_sent_list_with_word, candidate_sent_list_with_word, ngrams_num, hash_prime))
=======
        candidate[0]['Content'])
    candidate_sent_list_with_word = list(
        map(lambda sent: VieSentence(sent), candidate_sent_list))
    evidence = Evidence(candidate[0]['Title'], StringBasedTechnique.n_gram_matching(
        input_sent_list_with_word, candidate_sent_list_with_word, 6, 101))
>>>>>>> 9fb4ce608c92002bb74492b37036502364db2539
    result.addEvidence(evidence)

result.print()
