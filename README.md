﻿# 한케어봇
## 1. 제작 동기
당시 제가 포장 아르바이트를 하던 도중 한 사무직 직원이 저에게 다가와 특정 주문건을 반복해서 삭제해야 하는 작업이 추가되어 자신의 업무에 집중하기 어렵다고 한탄을 했습니다.

해당 작업을 빠르게 처리하지 않으면 물류 창고에서 일하는 직원분들이 새로운 주문 건을 늦게 확인하게 되고, 주문이 밀리게 되어, 특정 주문건을 빠르게 처리하지 못하는 사무직 직원들을 원망하는 상황이 만들어지게 되었습니다.

하지만 사무직 직원분들은 자기 일을 하다가 틈이 날 때마다 직급 상관 없이 특정 주문건을 일일이 찾아 처리하고 있었습니다. 하지만, 짧은 시간 동안 많은 주문건이 쌓이기 때문에, 물류 직원이 원망하지 않을 정도로 주문건을 처리하는 것은 매우 어려운 상황이었습니다.

저는 해당 문제를 놓치지 않고 해결하기 위해 노력했습니다. 쉬는 시간이나 틈날 때 사무실에 들어가 파이썬을 사용하여 특정 주문건을 자동으로 처리해주는 프로그램을 개발하고 배포했습니다. 이를 통해 반복적인 작업을 더 이상 하지 않게 된 사무직 직원들은 자신의 업무에 집중할 수 있게 되었고, 물류 창고 직원들도 해당 주문건이 빠르게 처리되어 주문이 밀리는 일이 크게 줄어들었습니다. 결과적으로 해당 프로그램으로 인해 사무직과 물류 창고 간의 원망이 점점 해소되었습니다.

물류 창고 포장 아르바이트에서 사무직으로 승격되어 일하던 중, 낮 12시마다 VIP 고객 중 입금 전인 고객의 입금 상태를 변경하지 못해, 크게 혼이 났던 적이 있습니다. 이를 계기로 한케어 봇에 자동으로 입금 처리까지 하는 기능을 추가하여, 저뿐만 아니라 다른 사무직 직원들이 더 이상 VIP 고객 입금 상태를 확인하지 않고 편히 일을 할 수 있는 환경을 만들었습니다.

## 2. 동작 설계
![한케어봇 drawio](https://github.com/coldsteelpope/haancare_bot/assets/128117575/4284b68d-64b8-4f67-a1b8-be47854a10bc)

## 3. 사용 기술
<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> <img src="https://img.shields.io/badge/selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white">

## 4. 기능
### 4.1 배송메시지 추가 및 삭제
#### 배송 메시지 추가
![배송메시지추가](https://github.com/coldsteelpope/haancare_bot/assets/128117575/88785afb-48cb-41eb-b3b6-e67e2e3750f5)

#### 배송 메시지 삭제
![배송메시지삭제](https://github.com/coldsteelpope/haancare_bot/assets/128117575/99738b56-c033-4520-9825-e7feed655b82)

### 4.2. 입금 처리
![입금처리](https://github.com/coldsteelpope/haancare_bot/assets/128117575/46605db4-d3f5-4006-8c96-7d543eb90799)

### 4.3. 특정 주문건 대량 처리
#### 특정 주문건 검색
![배송준비중검색](https://github.com/coldsteelpope/haancare_bot/assets/128117575/626bf8b9-dd5a-4174-9ef8-0269da9ae5dc)

![배송중검색](https://github.com/coldsteelpope/haancare_bot/assets/128117575/8cb53f9b-d4a8-4a5f-9f2e-0ad5cd0012f9)

#### 특정 주문건 처리
![배송준비중완료](https://github.com/coldsteelpope/haancare_bot/assets/128117575/255df6a3-4730-4ce1-a6aa-e700025f315e)

![배송중완료처리](https://github.com/coldsteelpope/haancare_bot/assets/128117575/39a14c65-b71d-4924-9c47-a699a33fae14)

## 5. 결론
