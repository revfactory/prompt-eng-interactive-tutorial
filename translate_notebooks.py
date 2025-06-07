#!/usr/bin/env python3
"""
노트북 번역 도우미 스크립트
Jupyter notebook (.ipynb) 파일의 마크다운 셀을 한글로 번역하는 데 도움을 주는 스크립트입니다.
"""

import json
import os
import sys

# 번역 매핑 딕셔너리
translations = {
    "Tutorial How-To": "튜토리얼 사용 방법",
    "This tutorial **requires an API key** for interaction.": "이 튜토리얼은 상호작용을 위해 **API 키가 필요합니다**.",
    "If you don't have an API key, you can sign up for one via the": "API 키가 없다면 다음을 통해 가입할 수 있습니다:",
    "or view our": "또는 다음을 확인하세요:",
    "static tutorial answer key": "정적 튜토리얼 정답지",
    "instead.": "대신.",
    "How to get started": "시작하는 방법",
    "Clone this repository to your local machine.": "이 저장소를 로컬 머신에 복제합니다.",
    "Install the required dependencies by running the following command:": "다음 명령을 실행하여 필요한 종속성을 설치합니다:",
    "Set up your API key and model name. Replace": "API 키와 모델 이름을 설정합니다. 다음을 교체하세요:",
    "with your actual Anthropic API key.": "실제 Anthropic API 키로.",
    "Run the notebook cells in order, following the instructions provided.": "제공된 지침에 따라 노트북 셀을 순서대로 실행합니다.",
    "Usage Notes & Tips": "사용 참고사항 및 팁",
    "This course uses Claude 3 Haiku with temperature 0.": "이 과정은 temperature 0으로 설정된 Claude 3 Haiku를 사용합니다.",
    "We will talk more about temperature later in the course.": "temperature에 대해서는 과정 후반부에 더 자세히 다룰 것입니다.",
    "For now, it's enough to understand that these settings yield more deterministic results.": "지금은 이러한 설정이 더 결정적인 결과를 생성한다는 것을 이해하는 것으로 충분합니다.",
    "All prompt engineering techniques in this course also apply to previous generation legacy Claude models": "이 과정의 모든 프롬프트 엔지니어링 기법은 이전 세대 Claude 모델에도 적용됩니다",
    "You can use": "다음을 사용할 수 있습니다:",
    "to execute the cell and move to the next one.": "셀을 실행하고 다음 셀로 이동합니다.",
    "When you reach the bottom of a tutorial page, navigate to the next numbered file in the folder": "튜토리얼 페이지의 끝에 도달하면 폴더의 다음 번호 파일로 이동하세요",
    "or to the next numbered folder if you're finished with the content within that chapter file.": "또는 해당 챕터 파일의 내용을 완료했다면 다음 번호 폴더로 이동하세요.",
    "The Anthropic SDK & the Messages API": "Anthropic SDK & Messages API",
    "We will be using the": "다음을 사용할 것입니다:",
    "and the": "그리고",
    "throughout this tutorial.": "이 튜토리얼 전체에서.",
    "Below is an example of what running a prompt will look like in this tutorial.": "아래는 이 튜토리얼에서 프롬프트를 실행하는 모습의 예시입니다.",
    "First, we create": "먼저, 다음을 생성합니다:",
    "which is a helper function that sends a prompt to Claude and returns Claude's generated response.": "이는 Claude에게 프롬프트를 보내고 Claude의 생성된 응답을 반환하는 헬퍼 함수입니다.",
    "Run that cell now.": "지금 그 셀을 실행하세요.",
    "Now we will write out an example prompt for Claude and print Claude's output by running our": "이제 Claude를 위한 예시 프롬프트를 작성하고 다음을 실행하여 Claude의 출력을 출력합니다:",
    "helper function.": "헬퍼 함수.",
    "Running the cell below will print out a response from Claude beneath it.": "아래 셀을 실행하면 그 아래에 Claude의 응답이 출력됩니다.",
    "Feel free to play around with the prompt string to elicit different responses from Claude.": "Claude로부터 다른 응답을 이끌어내기 위해 프롬프트 문자열을 자유롭게 변경해 보세요.",
    "The": "",
    "and": "와",
    "variables defined earlier will be used throughout the tutorial.": "앞서 정의된 변수들은 튜토리얼 전체에서 사용됩니다.",
    "Just make sure to run the cells for each tutorial page from top to bottom.": "각 튜토리얼 페이지의 셀을 위에서 아래로 실행하는 것을 잊지 마세요."
}

def translate_text(text):
    """간단한 문자열 대체 기반 번역"""
    translated = text
    for eng, kor in translations.items():
        translated = translated.replace(eng, kor)
    return translated

def translate_notebook(input_path, output_path):
    """노트북 파일을 번역합니다"""
    
    # JSON 파일로 읽기
    with open(input_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # 각 셀 번역
    for cell in notebook.get('cells', []):
        if cell.get('cell_type') == 'markdown':
            # 마크다운 셀의 source 번역
            source = cell.get('source', [])
            if isinstance(source, list):
                translated_source = []
                for line in source:
                    translated_source.append(translate_text(line))
                cell['source'] = translated_source
            elif isinstance(source, str):
                cell['source'] = translate_text(source)
    
    # 번역된 노트북 저장
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(notebook, f, ensure_ascii=False, indent=1)
    
    print(f"번역 완료: {input_path} -> {output_path}")

def main():
    """메인 함수"""
    # Anthropic 1P 폴더의 노트북 파일들
    notebook_files = [
        "00_Tutorial_How-To.ipynb",
        "01_Basic_Prompt_Structure.ipynb",
        "02_Being_Clear_and_Direct.ipynb",
        "03_Assigning_Roles_Role_Prompting.ipynb",
        "04_Separating_Data_and_Instructions.ipynb",
        "05_Formatting_Output_and_Speaking_for_Claude.ipynb",
        "06_Precognition_Thinking_Step_by_Step.ipynb",
        "07_Using_Examples_Few-Shot_Prompting.ipynb",
        "08_Avoiding_Hallucinations.ipynb",
        "09_Complex_Prompts_from_Scratch.ipynb",
        "10.1_Appendix_Chaining Prompts.ipynb",
        "10.2_Appendix_Tool Use.ipynb",
        "10.3_Appendix_Search & Retrieval.ipynb"
    ]
    
    base_dir = "/home/runner/work/prompt-eng-interactive-tutorial/prompt-eng-interactive-tutorial/Anthropic 1P"
    
    print("노트북 번역을 시작합니다...")
    print(f"번역할 파일 수: {len(notebook_files)}")
    print()
    
    for notebook_file in notebook_files:
        input_path = os.path.join(base_dir, notebook_file)
        output_path = input_path  # 원본 파일을 덮어씁니다
        
        if os.path.exists(input_path):
            try:
                translate_notebook(input_path, output_path)
            except Exception as e:
                print(f"오류 발생 {notebook_file}: {e}")
        else:
            print(f"파일을 찾을 수 없습니다: {input_path}")
    
    print("\n번역 작업이 완료되었습니다!")

if __name__ == "__main__":
    main()