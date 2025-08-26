# Задание 1. Проектирование технологической архитектуры

1. Ссылка на диаграмму: [диаграмма](https://drive.google.com/file/d/1BZMRKIRNivKBhdJrroqIkwr0kxoFUoeP/view?usp=sharing, "диаграмма")

## Стратегия масштабирования и отказоустойчивости

1. Горизонтальное масштабирование
2. Использование нескольких зон доступности
3. Managed Service for Kubernetes. Один кластер across AZ

## Балансировка нагрузки

1. Application Load Balancer. Приложение будет смотреть по health check куда отправлять запрос
2. Geobalancing. Выбор ближайшего разгруженного узла

## Фейловер-стратегия

1. Active-Active для приложения
2. Active-Passive для DB

## Конфигурацию DB

1. Managed Service for PostgreSQL
2. Primary (Master)
3. Synchronous Replica, hot standby
4. Asynchronous Replica для аналитики, бэкапов
5. WAL архтвация

### SLA

1. rate-limiting по ip и headers
2. grafana alerting для быстрой реакции на инциденты