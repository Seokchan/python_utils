Readme 파일 테스트

# EHS 프로젝트 소스 코드 분석

## 💻 파일 분석 데이터베이스

| Package | File Name | Role & Key Features | Key Business Logic | Main Tables (Estimated) |
| :--- | :--- | :--- | :--- | :--- |
| `com.ehs.EHS01.EHS01001` | **EHS01001Controller.java** | **API 진입점**<br>- 제품 목록/상세 조회<br>- 제품 저장/복사/삭제/복구<br>- 기초 코드(부서, 공정 등) 조회 | 제품(Item) 관련 모든 HTTP 요청을 받아 적절한 서비스로 전달합니다. | - 제품 마스터<br>- 제품-성분/규제 관계<br>- 기초 코드(부서, 공정 등) |
| `com.ehs.EHS01.EHS01001` | **EHS01001ServiceImpl.java** | **비즈니스 로직 구현체**<br>- 복합 조회<br>- JSON 직렬화 저장<br>- 트랜잭션 관리 | **1. 복합 조회:** 제품 상세 조회 시 정보, 성분, 규제 목록을 각각 조회하여 하나의 DTO로 조립<br>**2. JSON 직렬화:** 성분/규제 목록을 JSON 문자열로 변환하여 DB 프로시저 등으로 전달 | (상동) |
| `com.ehs.EHS01.EHS01002` | **EHS01002Controller.java** | **API 진입점**<br>- 코드 조회/저장/삭제 | 제품 관리에 필요한 기초 코드(용도, 보관방법, 단위)의 CRUD API를 제공합니다. | - 공통 코드 테이블 |
| `com.ehs.EHS01.EHS01002` | **EHS01002ServiceImpl.java** | **비즈니스 로직 구현체**<br>- 일괄 저장 및 롤백 | **일괄 트랜잭션:** 리스트로 받은 여러 코드 데이터를 순차적으로 저장하다가 하나라도 실패하면 전체 롤백(`@Transactional`) | (상동) |
| `com.ehs.EHS01.EHS01003` | **EHS01003Controller.java** | **API 진입점**<br>- 규제 성분 목록/상세 조회<br>- 규제 정보 저장/삭제 | 성분별 규제 정보의 CRUD API를 제공합니다. | - 규제 성분 마스터 |
| `com.ehs.EHS01.EHS01003` | **EHS01003ServiceImpl.java** | **비즈니스 로직 구현체**<br>- UI 포맷팅<br>- 일괄 저장 | **1. UI 포맷팅:** DB의 'Y'/'N' 값을 화면 표시용 체크(✓) 기호로 변환<br>**2. 일괄 트랜잭션:** 리스트 단위 저장 및 에러 시 롤백 | (상동) |
| `com.ehs.EHS01.EHS01004` | **EHS01004Controller.java** | **API 진입점**<br>- 작업 그룹(Group) CRUD<br>- 상세 작업(Task) CRUD | EHS 작업 분류(대분류, 소분류)를 계층적으로 관리하는 API를 제공합니다. | - 작업 그룹 테이블<br>- 작업 상세 테이블 |
| `com.ehs.EHS01.EHS01004` | **EHS01004ServiceImpl.java** | **비즈니스 로직 구현체**<br>- 삭제 유효성 검사<br>- 데이터 변환 저장 | **1. 삭제 방어:** 하위 데이터가 존재하면 삭제를 막는 유효성 검사 로직 포함<br>**2. 메타데이터 주입:** 저장 시 등록/수정일 등 시스템 정보를 추가하여 저장 | (상동) |
