# 자판기 시뮬레이터 (Vending Machine Simulator)

## 목적 (Purpose) 
이 프로젝트는 간단한 콘솔 기반의 자판기 시뮬레이터입니다. 사용자는 돈을 투입하고, 원하는 음료를 선택하여 구매할 수 있으며, 잔액이 부족할 경우 경고 메시지가 출력됩니다. 반복적인 구매와 종료 rl능   을 통해 기본적인 흐름 제어 및 사용자 입력 처리 능력을 학습할 수 있도록 설계되었습니다.

## 상세 기능 (Features)
 - 처음 실행할 떄는 coin변수를 0으로 선언해주면서 시작합니다.
 - 처음 사용자 입력란이 뜨는데 그 칸에는 본인이 보유하고 있는 금액을 입력합니다
 - 다음으로 총 5가지의 메뉴가 있는데 5개 메뉴 중 하나를 선택을 합니다. 만약 메뉴에 없는 번호를 선택할 시에는 '없는 메뉴'라는 메시지가 뜨고 다시 돌아갑니다. 그리고 우유 (1800원)을 구매를 하고 싶은데 돈을 1500원을 보유하고 있을시 '잔액부족'이라는 문구가 뜨고 그냥 종료(q)를 할건지 아니면 금액을 보충해서 구매(c)를 할 것인지에 대한 의사를 물어 봅니다.
     1. 오렌지주스 : 1500원
     2. 아메리카노 : 1500원
     3. 우유 : 1800
     4. 카페모카 : 2500원
     5. 아이스티 : 2000원
 - 금액이 충분히 있을시 음료를 구매를 하면 '현재 잔액'을 알려주고 마지막으로 그대로 종료를 할 것인지 아니면 추가 구매할 것인지 물어보고 종료(q)를 하면 그대로 끝이나고, 추가 구매(c)를 하면 돈을 보충할 것인지 안할 것인지 물어보고 처음 초기 입력 값으로 돌아갑니다.
 - 마지막으로 'q'를 입력하면 잔액을 반환해주고 프로그램이 종료가 됩니다.

## 입출력 형태 (in/output)
 - 입력
  1. 돈을 추가하시겠습니까? -> 'y' or 'n' <=== 잔액 부족하거나, 구매를 완료할 떄 뜹니다.
  2. 돈을 넣으세요. -> 정수(금액)
  3. 음료 번로 입력 -> 1~5(메뉴 선택)
  4. q 또는 c -> 종료 또는 계속 구매
- 출력
  1. 남은 잔액 출력
  2. 잔액 부족 시 '잔액부족' 출력
  3. 메뉴 선택 오류 시 '없는 메뉴' 출력
  4. 프로그램 종료 시 'n원이 반환되었습니다' 출력
 
## 실행방법
 1. Python 3.0 이 설치가 되어 있어야 합니다. 만약 없으시다면 (https://www.python.org/)에서 다운 받고 오시길 바랍니다.
 2. 그 다음은 vscode를 다운 받아야 합니다. 여기도 없으시다면 (https://code.visualstudio.com/)에서 vscode를 다운 받고 오시길 바랍니다.
 3. 이제 1, 2번 과정이 끝났으면 vscode에 들어가서 Python 확장자를 설치해주시길 바랍니다.
 4. 확장자까지 다운이 끝났으면 다운로드 받은 2244128.py 파일을 vscode로 열어주시길 바랍니다.
 5. 실행해서 위 상세기능과 입출력 형태를 참고하여 이용해주시길 바랍니다.
