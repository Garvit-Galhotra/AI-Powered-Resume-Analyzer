---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:13
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: AI engineer skilled in deep learning, computer vision, and NLP.
  sentences:
  - Detail-oriented Web Developer with experience in front-end development using HTML,
    CSS, JavaScript, and CMS platforms like WordPress and Webflow. Skilled in developing
    and maintaining websites, optimizing for speed, performance, and mobile responsiveness
    to ensure seamless user experiences. Proficient in troubleshooting issues, conducting
    routine maintenance, and implementing updates. Strong collaboration with designers
    and marketers to create functional, visually appealing digital experiences. A
    quick learner with a strong sense of UX design and problem-solving skills, and
    comfortable working in a remote environment. Passionate about continuous improvement
    and eager to learn new platforms and tools to deliver high-quality web solutions.
  - Looking for an AI specialist with expertise in neural networks and language models.
  - Artificial Intelligence engineer experienced in deep learning, NLP, and computer
    vision.
- source_sentence: Results-driven Web Developer with over 2 years of hands-on experience
    in front-end and back-end development, specializing in responsive, high-performance
    web applications. Proficient in HTML, CSS, JavaScript, and React, with strong
    expertise in back-end development using Node.js and Python. Experienced in troubleshooting,
    debugging, and optimizing web applications for performance and functionality.
    Skilled in UI/UX collaboration to implement modern design concepts and deliver
    user-friendly web experiences across platforms. Adept at working in Agile environments,
    applying best practices in front-end and back-end development. Passionate about
    contributing to AI-first operations and AI for Good initiatives, making a societal
    impact through innovative solutions. Thrives in remote work settings, with proven
    skills in time management, self-discipline, and effective collaboration.
  sentences:
  - Soul AI, founded by alumni from IIT Bombay and IIM Ahmedabad, is a fast-growing
    company specializing in high-quality human-curated data, AI-first scaled operations
    services, and more. Based in SF and Hyderabad, the company is driven by a passionate
    team focused on delivering AI for Good to create a positive societal impact. We
    are looking for a Web Developer with 2+ years of experience to design and develop
    responsive, high-performance web applications that offer exceptional user experiences
    across multiple platforms. The role involves collaborating with the UI/UX design
    team to implement modern design concepts and troubleshooting issues to ensure
    seamless functionality. The ideal candidate will have strong expertise in HTML,
    CSS, JavaScript, and frameworks like React or Angular, along with experience in
    back-end development using Node.js, Python, or similar technologies. Join us to
    enjoy competitive pay of ₹1200/hour, flexible hours, and remote work opportunities,
    with the potential to earn up to ₹108K per month once you clear our screening
    process.
  - Experienced backend developer skilled in Python, Django, RESTful APIs, and AWS.
  - Passionate and skilled Web Developer with over 2 years of experience in designing
    and developing responsive, high-performance web applications using HTML, CSS,
    JavaScript, and React, with a strong understanding of back-end development using
    Node.js, Python, and similar technologies. Proficient in creating seamless, user-friendly
    experiences across multiple platforms, collaborating closely with UI/UX teams
    to implement modern design concepts. Adept at troubleshooting, debugging, and
    optimizing web applications for functionality and performance. Experienced in
    working in Agile environments and applying best practices in both front-end and
    back-end development. Passionate about contributing to AI-first operations and
    AI for Good initiatives, with a strong commitment to innovation and societal impact
    in a fast-paced, remote work environment.
- source_sentence: Data scientist with experience in machine learning, deep learning,
    and big data analytics.
  sentences:
  - Data scientist proficient in Python, TensorFlow, NLP, and big data analytics.
  - Hiring a data scientist with strong Python, TensorFlow, and NLP expertise.
  - Certified Agile project manager with expertise in Scrum, Kanban, and leadership.
- source_sentence: UX/UI designer proficient in Adobe XD, Figma, and user research.
  sentences:
  - Hiring a UI/UX designer skilled in wireframing, prototyping, and design systems.
  - Creative UI/UX designer with experience in wireframing, prototyping, and user
    experience research.
  - Experienced QA Automation Engineer with 4-6 years of hands-on expertise in Playwright,
    Rest Assured, and Karate Labs. Skilled in developing, maintaining, and executing
    automated test scripts for web applications and APIs. Proficient in designing
    and implementing automated test frameworks, collaborating with cross-functional
    teams in an Agile environment, and contributing to CI/CD pipelines. Strong problem-solving
    abilities, attention to detail, and a proven track record of working independently
    in a remote setup. Familiar with API testing, continuous integration, and test
    automation best practices.
- source_sentence: 'Experienced Web Developer skilled in HTML, CSS, JavaScript, and
    React, with a basic understanding of back-end development using Node.js and Python.
    Adept at creating responsive, user-friendly websites and developing back-end APIs
    to enhance functionality and user experience. Strong problem-solving skills with
    a collaborative mindset, and a passion for contributing to sustainability and
    projects aimed at real environmental change. Proven ability to work effectively
    in Agile teams within a remote-friendly environment. Eager to leverage my expertise
    in front-end and back-end development to create impactful web solutions at a company
    with a meaningful mission.



    '
  sentences:
  - We are looking for a candidate with experience in HTML, CSS, and JavaScript, with
    knowledge of React or similar frameworks being a plus. A basic understanding of
    backend development using Node.js, Python, or similar technologies is desired.
    The ideal candidate should have the ability to collaborate effectively, solve
    problems efficiently, and share an interest in sustainability and making a positive
    impact. By joining us, you'll have the opportunity to work on projects that contribute
    to real environmental change. We offer a flexible, remote-friendly work environment,
    and the chance to be part of a growing company with a meaningful mission.
  - Experienced Web Developer skilled in HTML, CSS, JavaScript, and React, with a
    basic understanding of backend development using Node.js and Python. Adept at
    creating responsive, user-friendly websites and developing backend APIs. Strong
    problem-solving skills and a collaborative approach, with a passion for sustainability
    and contributing to projects that support real environmental change. Proven ability
    to work effectively in Agile teams within a remote-friendly environment. Enthusiastic
    about joining a company with a meaningful mission, where I can leverage my expertise
    in front-end and back-end development to create impactful web solutions.
  - Experienced Web Developer with expertise in both front-end and back-end development.
    Skilled in web design, programming, and maintaining websites to ensure optimal
    functionality and performance. Proficient in various programming languages like
    HTML, CSS, JavaScript, and PHP, with a strong focus on creating user-friendly
    and responsive websites. Adept at problem-solving, website optimization, and working
    in both team and independent settings. Holds a Bachelor's degree in Computer Science
    and has experience in digital marketing.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Experienced Web Developer skilled in HTML, CSS, JavaScript, and React, with a basic understanding of back-end development using Node.js and Python. Adept at creating responsive, user-friendly websites and developing back-end APIs to enhance functionality and user experience. Strong problem-solving skills with a collaborative mindset, and a passion for contributing to sustainability and projects aimed at real environmental change. Proven ability to work effectively in Agile teams within a remote-friendly environment. Eager to leverage my expertise in front-end and back-end development to create impactful web solutions at a company with a meaningful mission.\n\n\n',
    'Experienced Web Developer skilled in HTML, CSS, JavaScript, and React, with a basic understanding of backend development using Node.js and Python. Adept at creating responsive, user-friendly websites and developing backend APIs. Strong problem-solving skills and a collaborative approach, with a passion for sustainability and contributing to projects that support real environmental change. Proven ability to work effectively in Agile teams within a remote-friendly environment. Enthusiastic about joining a company with a meaningful mission, where I can leverage my expertise in front-end and back-end development to create impactful web solutions.',
    "We are looking for a candidate with experience in HTML, CSS, and JavaScript, with knowledge of React or similar frameworks being a plus. A basic understanding of backend development using Node.js, Python, or similar technologies is desired. The ideal candidate should have the ability to collaborate effectively, solve problems efficiently, and share an interest in sustainability and making a positive impact. By joining us, you'll have the opportunity to work on projects that contribute to real environmental change. We offer a flexible, remote-friendly work environment, and the chance to be part of a growing company with a meaningful mission.",
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 13 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, <code>sentence_2</code>, and <code>label</code>
* Approximate statistics based on the first 13 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          | sentence_2                                                                          | label                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              | string                                                                              | float                                                          |
  | details | <ul><li>min: 15 tokens</li><li>mean: 64.92 tokens</li><li>max: 172 tokens</li></ul> | <ul><li>min: 17 tokens</li><li>mean: 60.77 tokens</li><li>max: 160 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 82.31 tokens</li><li>max: 216 tokens</li></ul> | <ul><li>min: 0.6</li><li>mean: 0.79</li><li>max: 0.9</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_2                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | label             |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Experienced QA Automation Engineer with 4-6 years of expertise in Playwright, Rest Assured, and Karate Labs. Skilled in developing and executing automated test scripts for web applications and APIs, as well as designing and implementing automated test frameworks. Proficient in working in an Agile environment and contributing to CI/CD pipelines. Strong in API testing, continuous integration, and test automation best practices, with a proven track record of working independently in a remote setup. Demonstrates excellent problem-solving skills, attention to detail, and the ability to deliver results autonomously.<br><br><br></code>                                                                                                                                                                              | <code>Experienced QA Automation Engineer with 4-6 years of hands-on expertise in Playwright, Rest Assured, and Karate Labs. Skilled in developing, maintaining, and executing automated test scripts for web applications and APIs. Proficient in designing and implementing automated test frameworks, collaborating with cross-functional teams in an Agile environment, and contributing to CI/CD pipelines. Strong problem-solving abilities, attention to detail, and a proven track record of working independently in a remote setup. Familiar with API testing, continuous integration, and test automation best practices.</code>                                                                                                                                               | <code>We are seeking a skilled QA Automation Engineer with 4-6 years of hands-on experience to join our team immediately. The ideal candidate will have expertise in Playwright, Rest Assured, and Karate Labs, and be proficient in developing, maintaining, and executing automated test scripts for web applications and APIs. You will be responsible for designing and implementing automated test frameworks, ensuring seamless testing processes, and collaborating closely with developers and cross-functional teams to deliver high-quality products. The role involves working in an Agile environment, continuously improving test processes, and contributing to CI/CD pipelines. Strong problem-solving skills, attention to detail, and the ability to work independently in a remote setup are essential. Familiarity with CI/CD practices and tools is also required for integrating testing into the delivery pipeline.</code>                                                                                                         | <code>0.65</code> |
  | <code>Detail-oriented Web Developer with expertise in front-end development using HTML, CSS, JavaScript, and CMS platforms such as WordPress and Webflow. Experienced in developing and maintaining websites, optimizing for speed, performance, and mobile responsiveness to deliver seamless user experiences. Skilled in troubleshooting issues, conducting routine maintenance, and implementing necessary updates. Proven ability to collaborate with designers and marketers to create functional, visually appealing digital experiences. Adept at problem-solving with a strong focus on UX design and user-centered development. Comfortable working in a remote environment, with a passion for continuous learning and improvement. Eager to adopt new platforms and tools to deliver high-quality, innovative web solutions.</code> | <code>Detail-oriented Web Developer with experience in front-end development using HTML, CSS, JavaScript, and CMS platforms like WordPress and Webflow. Skilled in developing and maintaining websites, optimizing for speed, performance, and mobile responsiveness to ensure seamless user experiences. Proficient in troubleshooting issues, conducting routine maintenance, and implementing updates. Strong collaboration with designers and marketers to create functional, visually appealing digital experiences. A quick learner with a strong sense of UX design and problem-solving skills, and comfortable working in a remote environment. Passionate about continuous improvement and eager to learn new platforms and tools to deliver high-quality web solutions.</code> | <code>We are looking for a Web Developer to develop and maintain websites using HTML, CSS, JavaScript, and CMS platforms like WordPress or Webflow. The role involves collaborating with designers and marketers to create functional and visually appealing digital experiences, optimizing websites for speed, performance, and mobile responsiveness. You will troubleshoot issues, conduct routine maintenance, and apply updates as necessary. In this fully remote role, you’ll be part of a collaborative team where your ideas are valued, and you’ll have opportunities to learn and grow. We’re looking for someone with a basic understanding of front-end development and a willingness to learn WordPress, Webflow, or similar platforms. A strong sense of design, layout, and user experience, as well as problem-solving skills and proactive learning, are key to success in this position. We offer flexible working hours, impactful projects with growth potential, and the chance to work with global clients across vari...</code> | <code>0.78</code> |
  | <code>UX/UI designer proficient in Adobe XD, Figma, and user research.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | <code>Creative UI/UX designer with experience in wireframing, prototyping, and user experience research.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | <code>Hiring a UI/UX designer skilled in wireframing, prototyping, and design systems.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | <code>0.82</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `tp_size`: 0
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Framework Versions
- Python: 3.12.4
- Sentence Transformers: 4.0.1
- Transformers: 4.50.3
- PyTorch: 2.6.0+cpu
- Accelerate: 1.5.2
- Datasets: 3.5.0
- Tokenizers: 0.21.1

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->