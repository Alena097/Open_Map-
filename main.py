 sf::RenderWindow window(sf::VideoMode(800, 600), "SFML Example"); // Создание окна размером 800x600 пикселей с заголовком "SFML Example"
sf::RectangleShape button(sf::Vector2f(100, 50)); // Создание прямоугольника (кнопки) размером 100x50 пикселей
button.setPosition(50, 500); // Установка позиции кнопки на экране
button.setFillColor(sf::Color::Green); // Установка цвета кнопки (зеленый)

sf::Font font; // Создание объекта шрифта
if (!font.loadFromFile("Rubik.ttf")) {
    return 1; 
}

sf::Text buttonText("Найти", font, 20); 
buttonText.setFillColor(sf::Color::Black);
buttonText.setPosition(60, 510); 

sf::RectangleShape startButton(sf::Vector2f(100, 50)); // Создание прямоугольника (кнопки) размером 100x50 пикселей
startButton.setPosition(200, 500); 
startButton.setFillColor(sf::Color::Blue); 

// Создание текста для второй кнопки "Начать"
sf::Text startButtonText("Начать", font, 20); 
startButtonText.setFillColor(sf::Color::Black); 
startButtonText.setPosition(210, 510); 

sf::RectangleShape screen(sf::Vector2f(700, 400)); 
screen.setPosition(50, 50); 
screen.setFillColor(sf::Color::Gray); 

sf::RectangleShape inputField(sf::Vector2f(200, 30)); 
inputField.setPosition(200, 510); 
inputField.setFillColor(sf::Color::White);
inputField.setOutlineThickness(2); 
inputField.setOutlineColor(sf::Color::Black);
sf::String inputText; // Создание объекта строки для хранения введенного текста
sf::Text inputTextDisplay("", font, 20); // Создание текстового объекта для отображения введенного текста размером 20 пикселей
inputTextDisplay.setFillColor(sf::Color::Gray); // Установка цвета текста отображения введенного текста (серый)
inputTextDisplay.setPosition(210, 515); // Установка позиции текста отображения введенного текста на экране (координаты x=210, y=515);

// Отобрази кнопку и экран в окне:
while (window.isOpen()) // Основной цикл отображения окна, выполняется, пока окно открыто
{
    sf::Event event; // Создание объекта события
    while (window.pollEvent(event)) // Проверка и обработка событий в очереди
    {
        if (event.type == sf::Event::Closed) // Если событие - закрытие окна
            window.close(); // Закрыть окно
    }

    window.clear(); // Очистка содержимого окна

    // Отрисовка экрана, кнопки и текста на кнопке
    window.draw(screen); // Отрисовка экрана
    window.draw(button); // Отрисовка кнопки
    window.draw(buttonText); // Отрисовка текста на кнопке
    window.draw(startButton); // Отрисовка второй кнопки "Начать"
    window.draw(startButtonText); // Отрисовка текста на второй кнопке "Начать"
    window.draw(inputField); // Отрисовка поля ввода
    window.draw(inputTextDisplay); // Отрисовка текста на поле ввода

    window.display(); // Отображение содержимого окна

} // Конец основного цикла

return 0; // Возврат успешного завершения программы
