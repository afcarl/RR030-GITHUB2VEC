
GITHUB2VEC:

Github2Vec is a WIP. It's intended purpose is to act as a personal productivity tool to provide prompt feedback as to repos with specific TAGS, and a quantitative indication of similar natured repros. As you are aware, the state of Github repo documentation varies from "none" to "extensive". As such, it is a bit of an evolving art to capture sufficient input for Gensim/DOC2VEC to make meaningful generaliations as to "Similar" and "DisSimilar" repo determinations. A toy data set of (1000) Github repos is provided located in ".\Github2Vec\1_Repo_data\github.com\afcarl\Github_Repo_html_txt_files_1000.zip".

************************************
START: Example of GITHUB2VEC Output:
************************************
GITHUB REPRO NAME: "ABC-GAN"

REPRO AUTHOR: "IGORSUSMELJ"

REPO TAGS: ['IMAGE', 'BLUR', 'LSUN', 'CONTROLLER', 'GAN']

MOST SIMILAR REPOS ArgMin(10,Score>0.5): [('ABC-GAN', 1.0), ('BICYCLEGAN-PYTORCH', 0.6996548175811768), ('6853-PROJECT', 0.6616806983947754), ('BICYCLEGAN-TENSORFLOW', 0.5852857828140259), ('ANIMEGAN', 0.5558176040649414), ('AC-GAN', 0.551661491394043), ('BAYESGAN', 0.5287083387374878), ('AGE', 0.5171400308609009)]

MOST SIMILAR REPOS TAGS: ['IMAGE', 'GAN', 'TRAIN', 'DATA', 'DATASET']

MOST DISSIMILAR REPOS ArgMin(10,Score<0.05): [('AWS-BIG-DATA-BLOG', 0.00018744543194770813), ('ARISTO-MINI', 0.00030460208654403687), ('A_COURSE_IN_TIMESERIES', 0.00031220726668834686), ('AIS_DEMO', 0.0003952424740418792), ('ADT_OPT', 0.0004009399563074112), ('BAYESIAN-KALMANFILTER', 0.0004142019897699356), ('AWESOME-AWESOME-AWESOME', 0.00048428773880004883), ('BAYES', 0.0006488114595413208), ('ARXIV-TOPICS', 0.0006780996918678284), ('2013_FALL_ASTR599', 0.0006959773600101471)]

MOST DISSIMILAR REPOS TAGS: ['AWS', 'BLOG', 'DATA']
************************************
END: Example of GITHUB2VEC Output:
************************************


1. Pre-Requisits:

1a. https://github.com/muhasturk/gitim (Optional)

1b. https://github.com/jgm/pandoc

1c. https://github.com/afcarl/gensim-simserver-WORKS

1d. https://github.com/afcarl/sqlitedict-WORKS_W_SIMSERVER

2. Create your Github Repo collection.

3. Create a local copy of your Github Repo collection using https://github.com/muhasturk/gitim (Optional).

4. Create a list file for all Repos using local copy folder ( dir /b *.* > output.dat ).

5. Create html files for each Repo Webpage using: ./1_Repo_data/WP_copy_B.py, using "output.dat" as input.

6. Create txt files for each Repo html file using: ./1_Repo_data/html_parse_H.py, using "output.dat" as input.

7. Create zipped dictionary files using: ./2_Gensim_Simserver/simserver_run_local_F2.py.
7a. Input #1: html_parse_H_ALL_LABELS_1000.txt
7b. Input #2: html_parse_H_ALL_1000.txt
7c. Input #3: forked_author_dict_1000.zpkl
7d. Input #4: forked_author_to_titles_dict_1000.zpkl
7e. Input #5: repo_title_set_1000.zpkl
7f. Input #6: words_alpha.txt


7g. OUTPUT #1: print("Similar: ", service.find_similar('02456-deep-learning', min_score=0.5, max_results=11))
Similar:  [('02456-deep-learning', 1.0, None), ('awesome-docker', 0.7814108729362488, None), ('alpine-minikube', 0.7373288869857788, None), ('baseimage-docker', 0.7281696796417236, None), ('attalos', 0.69722580909729, None), ('bazel-docker', 0.6071430444717407, None), ('basic-docker-agent-build', 0.5810653567314148, None), ('async-deep-rl', 0.5226494073867798, None), ('altair-Lab41', 0.5212352275848389, None)]

7h. OUTPUT #2: print("DisSimilar: ", service.find_dissimilar('02456-deep-learning', max_score=0.5, max_results=10))
DisSimilar:  [('attention-is-all-you-need-divyanshj16', 4.366040229797363e-05, None), ('allen', 0.00011094659566879272, None), ('bemkl', 0.00014548376202583313, None), ('backo', 0.00017013587057590485, None), ('aeropy-AeroPython', 0.000325517263263464, None), ('arduino-projects', 0.00038177333772182465, None), ('Asymmetric-Hashing-ANN', 0.000621844083070755, None), ('active-testing', 0.0006259661167860031, None), ('adaptive-neural-compilation', 0.0008356906473636627, None), ('amen', 0.0008382126688957214, None)]

7i. OUTPUT #3: print(service.find_similar(doc, min_score=0.5, max_results=11))
[('ASTRAL', 0.5314284563064575, None), ('annoy', 0.5216116905212402, None)]

7j. OUTPUT #4: doc_title_Similar_dict_1000.zpkl
7k. OUTPUT #5: doc_title_Similar_TAGS_dict_1000.zpkl
7l. OUTPUT #6: doc_title_Similar_TAGS_dict_all_1000.zpkl
7m. OUTPUT #7: doc_title_DisSimilar_dict_1000.zpkl
7n. OUTPUT #8: doc_title_DisSimilar_TAGS_dict_1000.zpkl
7o. OUTPUT #9: doc_title_DisSimilar_TAGS_dict_all_1000.zpkl









