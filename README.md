# Anthropic의 Prompt Engineering 인터랙티브 튜토리얼에 오신 것을 환영합니다

## 과정 소개 및 목표

이 과정은 Claude에서 최적의 프롬프트를 엔지니어링하는 방법을 단계별로 종합적으로 이해할 수 있도록 구성되었습니다.

**이 과정을 완료하면 다음을 할 수 있게 됩니다**:
- 좋은 프롬프트의 기본 구조 마스터하기
- 일반적인 실패 모드를 인식하고 이를 해결하는 '80/20' 기법 학습하기
- Claude의 강점과 약점 이해하기
- 일반적인 사용 사례에 대한 강력한 프롬프트를 처음부터 구축하기

## 과정 구조 및 내용

이 과정은 프롬프트 작성과 문제 해결을 직접 연습할 수 있는 많은 기회를 제공하도록 구성되었습니다. 과정은 **연습 문제가 포함된 9개의 챕터**와 더 고급 방법을 다루는 부록으로 구성되어 있습니다. **챕터 순서대로 과정을 진행하는 것을 권장합니다**. 

**각 레슨에는 하단에 "Example Playground" 영역**이 있어 레슨의 예제를 자유롭게 실험하고 프롬프트 변경이 Claude의 응답을 어떻게 바꾸는지 직접 확인할 수 있습니다. [정답지](https://docs.google.com/spreadsheets/d/1jIxjzUWG-6xBVIa2ay6yDpLyeuOh_hR_ZB75a47KX_E/edit?usp=sharing)도 제공됩니다.

참고: 이 튜토리얼은 가장 작고, 빠르며, 저렴한 모델인 Claude 3 Haiku를 사용합니다. Anthropic에는 [두 가지 다른 모델](https://docs.anthropic.com/claude/docs/models-overview)인 Claude 3 Sonnet과 Claude 3 Opus가 있으며, 이들은 Haiku보다 더 지능적이고, Opus가 가장 지능적입니다.

*이 튜토리얼은 [Anthropic의 Claude for Sheets 확장 프로그램을 사용하는 Google Sheets 버전](https://docs.google.com/spreadsheets/d/19jzLgRruG9kjUQNKtCg1ZjdD6l6weA6qRXG5zLIAhC8/edit?usp=sharing)도 제공됩니다. 더 사용자 친화적이므로 해당 버전을 사용하는 것을 권장합니다.*

시작할 준비가 되면 아래 목차에서 원하는 버전의 `01_Basic Prompt Structure`로 이동하여 진행하세요.

## 튜토리얼 버전 선택

이 저장소는 세 가지 버전의 튜토리얼을 제공합니다:

- **[Anthropic 1P](./Anthropic%201P/)**: Anthropic의 직접 API를 사용하는 버전
- **[AmazonBedrock (Anthropic)](./AmazonBedrock/anthropic/)**: Amazon Bedrock에서 Anthropic API를 사용하는 버전  
- **[AmazonBedrock (boto3)](./AmazonBedrock/boto3/)**: Amazon Bedrock에서 boto3 라이브러리를 사용하는 버전

## 목차

각 챕터는 레슨과 연습 문제 세트로 구성되어 있습니다.

### 시작하기
- **Chapter 0:** 튜토리얼 사용법
  - [Anthropic 1P](./Anthropic%201P/00_Tutorial_How-To.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/00_Tutorial_How-To.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/00_Tutorial_How-To.ipynb)

### 초급
- **Chapter 1:** 기본 프롬프트 구조
  - [Anthropic 1P](./Anthropic%201P/01_Basic_Prompt_Structure.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/01_Basic_Prompt_Structure.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/01_Basic_Prompt_Structure.ipynb)

- **Chapter 2:** 명확하고 직접적으로 표현하기
  - [Anthropic 1P](./Anthropic%201P/02_Being_Clear_and_Direct.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/02_Being_Clear_and_Direct.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/02_Being_Clear_and_Direct.ipynb)

- **Chapter 3:** 역할 할당하기
  - [Anthropic 1P](./Anthropic%201P/03_Assigning_Roles_Role_Prompting.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/03_Assigning_Roles_Role_Prompting.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/03_Assigning_Roles_Role_Prompting.ipynb)

### 중급 
- **Chapter 4:** 데이터와 지시사항 분리하기
  - [Anthropic 1P](./Anthropic%201P/04_Separating_Data_and_Instructions.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/04_Separating_Data_and_Instructions.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/04_Separating_Data_and_Instructions.ipynb)

- **Chapter 5:** 출력 형식 지정 및 Claude를 대신해서 말하기
  - [Anthropic 1P](./Anthropic%201P/05_Formatting_Output_and_Speaking_for_Claude.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/05_Formatting_Output_and_Speaking_for_Claude.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/05_Formatting_Output_and_Speaking_for_Claude.ipynb)

- **Chapter 6:** Precognition (단계별로 생각하기)
  - [Anthropic 1P](./Anthropic%201P/06_Precognition_Thinking_Step_by_Step.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/06_Precognition_Thinking_Step_by_Step.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/06_Precognition_Thinking_Step_by_Step.ipynb)

- **Chapter 7:** 예시 사용하기
  - [Anthropic 1P](./Anthropic%201P/07_Using_Examples_Few-Shot_Prompting.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/07_Using_Examples%20_Few-Shot_Prompting.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/07_Using_Examples_Few-Shot_Prompting.ipynb)

### 고급
- **Chapter 8:** Hallucination 방지하기
  - [Anthropic 1P](./Anthropic%201P/08_Avoiding_Hallucinations.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/08_Avoiding_Hallucinations.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/08_Avoiding_Hallucinations.ipynb)

- **Chapter 9:** 복잡한 프롬프트 구축하기 (산업별 사용 사례)
  - [Anthropic 1P](./Anthropic%201P/09_Complex_Prompts_from_Scratch.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/09_Complex_Prompts_from_Scratch.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/09_Complex_Prompts_from_Scratch.ipynb)

### 부록: 표준 프롬프팅을 넘어서
- **부록 1:** 프롬프트 연결하기
  - [Anthropic 1P](./Anthropic%201P/10.1_Appendix_Chaining%20Prompts.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/10_1_Appendix_Chaining_Prompts.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/10_1_Appendix_Chaining_Prompts.ipynb)

- **부록 2:** 도구 사용
  - [Anthropic 1P](./Anthropic%201P/10.2_Appendix_Tool%20Use.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/10_2_Appendix_Tool_Use.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/10_2_Appendix_Tool_Use.ipynb)

- **부록 3:** Search & Retrieval
  - [Anthropic 1P](./Anthropic%201P/10.3_Appendix_Search%20&%20Retrieval.ipynb) | [Bedrock (Anthropic)](./AmazonBedrock/anthropic/10_4_Appendix_Search_and_Retrieval.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/10_4_Appendix_Search_and_Retrieval.ipynb)

- **부록 4:** 경험적 성능 평가 (Bedrock 전용)
  - [Bedrock (Anthropic)](./AmazonBedrock/anthropic/10_3_Appendix_Empirical_Performance_Evaluations.ipynb) | [Bedrock (boto3)](./AmazonBedrock/boto3/10_3_Appendix_Empirical_Performance_Eval.ipynb)