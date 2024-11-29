# Task-name

### Paper

Title: "Evaluating language models as risk scores"

Abstract: 

Current question-answering benchmarks predominantly focus on accuracy in realizable prediction tasks.
Such benchmarks necessarily fail to evaluate LLMs' ability to quantify ground-truth outcome uncertainty. In this work, we focus on the use of LLMs as risk scores for unrealizable prediction tasks. We introduce folktexts, a software package to systematically generate risk scores using LLMs, and evaluate them against US Census data products. We find that zero-shot risk scores produced by multiple-choice question-answering have high predictive signal but are widely miscalibrated. Base models consistently overestimate outcome uncertainty, while instruction-tuned models underestimate uncertainty and produce over-confident risk scores. In fact, instruction-tuning polarizes answer distribution regardless of true underlying data uncertainty, revealing LLMs' general inability to express aleatoric data uncertainty.

Homepage: [https://github.com/socialfoundations/folktexts](https://github.com/socialfoundations/folktexts)


### Citation

```
@inproceedings{cruz2024evaluating,
    title={Evaluating language models as risk scores},
    author={Andr\'{e} F. Cruz and Moritz Hardt and Celestine Mendler-D\"{u}nner},
    booktitle={The Thirty-eight Conference on Neural Information Processing Systems Datasets and Benchmarks Track},
    year={2024},
    url={https://openreview.net/forum?id=qrZxL3Bto9}
}
```

### Groups, Tags, and Tasks

#### Groups

* `multiple_choice_qa`: Run folktexts benchmark tasks using multiple-choice Q&A.
* `numeric_qa`: Run folktexts benchmark tasks using numeric Q&A (also known as verbalized probabilities).

#### Tasks

* `task_name`: `1-sentence description of what this particular task does`
* `task_name2`: ...

### Checklist

For adding novel benchmarks/datasets to the library:
* [X] Is the task an existing benchmark in the literature?
  * [X] Have you referenced the original paper that introduced the task?
  * [X] If yes, does the original paper provide a reference implementation? If so, have you checked against the reference implementation and documented how to run such a test?


If other tasks on this dataset are already supported:
* [X] Is the "Main" variant of this task clearly denoted?
* [X] Have you provided a short sentence in a README on what each new variant adds / evaluates?
* [X] Have you noted which, if any, published evaluation setups are matched by this variant?
