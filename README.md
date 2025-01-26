```markdown
# Expense Tracker

[Expense Tracker](https://roadmap.sh/projects/expense-tracker) — это инструмент для учета расходов. Он позволяет добавлять, удалять расходы, а также просматривать список всех расходов и делать сводку по месяцам.

## Основные команды

### 1. Добавить расход
Для добавления нового расхода используйте команду `add`:

```bash
python expense_tracker.py add --description "Описание расхода" --amount 50.0
```

где:
- `--description` — описание расхода (например, "Ужин", "Транспорт").
- `--amount` — сумма расхода.

Пример:

```bash
python expense_tracker.py add --description "Coffee" --amount 5.5
```

### 2. Список всех расходов
Для просмотра всех расходов используйте команду `list`:

```bash
python expense_tracker.py list
```

Пример вывода:

```
ID   Date        Description         Amount
--------------------------------------------------
1    2025-01-25  Lunch               $20.0
2    2025-01-25  Coffee              $5.5
```

### 3. Удалить расход
Чтобы удалить расход по ID используйте команду `delete`:

```bash
python expense_tracker.py delete --id 1
```

где `--id` — это ID расхода, который вы хотите удалить.

### 4. Сводка расходов
Для получения общей суммы расходов используйте команду `summary`:

```bash
python expense_tracker.py summary
```

Для сводки по конкретному месяцу:

```bash
python expense_tracker.py summary --month 1
```

где `--month` — это номер месяца (например, 1 для января).

## Установка и запуск

1. Скачайте или клонируйте проект:
   ```bash
   git clone https://github.com/your-username/expense-tracker.git
   cd expense-tracker
   ```

2. Установите все зависимости (если они есть). Если требуется, создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows
   ```

3. Запустите трекер расходов:
   ```bash
   python expense_tracker.py
   ```

## Лицензия

Этот проект распространяется под лицензией MIT.
```

Замените `your-username` на ваш реальный GitHub username, и теперь URL вашего проекта будет корректно отображаться.
