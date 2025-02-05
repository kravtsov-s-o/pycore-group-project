## Personal Assistant - Jarlis
#### PyCore 17 group 6 project

## Персональний асистент допоможе у вам у повсякденному житті.

### Для встановлення пакету необхідно:
Проект реализован на менеджере `poetry` + `docker`:

**Сборка Docker-образа (перейдите в директорию с Dockerfile)**

`docker build -t my_personal_assistant .`

**Запуск контейнера**

`docker run -it my_personal_assistant`

Асистент зроблено у гарному, візуально комфортному вигляді, із простим для 
користувача інтерфейсом, де йому потрібно лише вибирати варіант команди,
а не вводити її самотужки, маючи великий шанс на помилку.

### Функціонал асистенту складається з:
1. Книга контактів
2. Нотатки
3. Сортування файлів.

Навігація по меню здійснюється за допомогою відповідних цифр.
В деяких місцях - літери.
Відповідні підказки будуть на екрані

Загальні правила - не використовувати порожні пробіли. Скрипт їх коректно 
опрацьовує, тож ви згаєте свій час.

### Сортування.

Сортувальник файлів буде відсортовувати файли за їх типом - зображення,
відео, аудіо, документи, архіви. Для кожного із цих типів буде створено
відповідну папку, якщо вона ще не створена, та файли будуть відсортовані
по відповідним папкам. Архіви будуть розпаковуватись у папки із відповідним
іменем всередині папки `ARCHIEVES`.

Для сортування необхідно вибрати відповідну опцію у меню, де вам буде 
запропоновано ввести шлях до папки, в якій необхідно провести сортування.

### Нотатки.

Список нотаток буде зберігати, знаходити, видаляти, редагувати нотатки,
а також додавати теги для вже створених нотаток.
Для додавання нової нотатки необхідно вибрати відповідну опцію, потім 
ввести валідні значення у таком порядку - `title;content;#tag1,#tag2,#tag3`.
- `Title` - Назва нотатки, обов'язкове поле. Повинна бути завдовжки мінімум 
3 символи та максимум 40 символів.
- `Content` - вміст нотатки, не обов'язкове поле. Може бути до 512 символів
довжиною. 
- `Tag` - тег для нотаток. Не обов'язкове поле, для однієї нотатки може бути
декілька тегів. Повинен починатись з обов'язкового символа `#` та бути 
мінімум 3 та максимум 40 символів довжиною. Сюди внесено окремий функціонал
по додаванню, видалянню тегів для нотатки, а також пошуку нотаток за тегами
та сортування їх у алфавітному порядку.

Редагувати можна як всю нотатку одразу, так і окремі її поля. 

### Книга контактів.

Книга контактів вміщує в собі записи про контакт, а саме - Ім'я, телефон,
день народження, електронна пошта, адреса. Функціонал Книги дозволяє 
додавати нові контакти, знаходити, видаляти, редагувати вже існуючі 
контакти. Також є окремий функціонал, за допомогою якого можна подивитись
список контактів, у яких день народження через задану кількість днів.
Для корректної обробки інформації формат додавання нового контакту є таким -
`name;phone;birthday;email;address`.
- `Name` - Ім'я контакта. Обов'язкове поле. Має бути мінім 3 символи у довжину
та не складатись лише із цифр.
- `Phone` - телефон, обов'язкове поле. Має систему валідації для телефонів 
операторів України.
- `Birthday` - дата народження, не обов'язкове поле. Має систему валідації на 
дійсність введеної дати. Формат введення - дд.мм.рррр.
- `Email` - електронна пошта, не обов'язкове поле, має систему валідації на 
дійсність введеного імейлу.
- `Address` - адреса, не обов'язкове поле. Тут зберігається адреса контакта.
Редагування контактів відбувається в двох режимах - як всього контакта, так 
і одного його поля. Відповідний функціонал буде у вас перед очима.

Також, додатково, для покращення візуалізації представлення знайдених 
контактів або нотаток, до функціоналу введена пагінація - буде виведено по 
10 контактів\нотаток на одну сторінку. В наявності є функціонал навігації 
по сторінкам.

Всі маніпуляції користувача будуть зберігатись на жорсткому диску, тож 
він не втрачатиме свої дані у разі припинення роботи із асистентом, весь 
функціонал та внесені дані будуть збережені.

Персональний асистент вільний у використанні, ліцензій не потребує.