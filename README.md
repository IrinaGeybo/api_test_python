**Учебный проект** 
Тестируем этот сайт  - https://restful-booker.herokuapp.com/apidoc/index.html

**Структура проекта**
* tests/ — тесты.
* conftest.py — общие фикстуры pytest, включая browser для работы с Jenkins.
* requirements.txt — Python-зависимости проекта.
* .env.example — шаблон локальных настроек.
* .github/workflows/run_tests.yml — запуск тестов в GitHub Actions.
* .gitignore — исключения для Git, включая локальный .env.