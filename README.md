# python-flask-docker
Итоговый проект (пример) курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy
API: flask
Данные: с kaggle - https://www.kaggle.com/andrewmvd/chocolate-ratings


Задача: предсказать рейтинг шоколада по его характеристикам. Задача регрессии

Используемые признаки:


- Company (Manufacturer) (text)
- Company Location (text)
- Review Date (int)
- Country of Bean Origin (text)
- Specific Bean Origin or Bar Name (text)
- Cocoa Percent (text)
- Ingredients (text)
- Most Memorable Characteristics (text)

Модель: RandomForestRegressor

### Клонируем репозиторий и создаем образ
```
$ git clone https://github.com/Alexidis/ml_for_buisness_api.git
$ cd ml_for_buisness_api
$ docker build -t Alexidis/ml_for_buisness_api .
```

### Запускаем контейнер

Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)
```
$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models Alexidis/ml_for_buisness_api
```

### Переходим на localhost:8181
