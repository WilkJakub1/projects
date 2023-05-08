#define _CRT_SECURE_NO_WARNINGS

#include <SFML/Graphics.hpp>
#include <iostream>
#include <stdlib.h>     
#include <time.h>   
#include <math.h>
#include <string> 


class Outro {
private:
    int x;
    int y;
    sf::Text text;
    sf::Font font;
public:
    Outro(int x, int y);
    void draw(sf::RenderWindow& window);
};

Outro::Outro(int x, int y) {
    this->x = x;
    this->y = y;
    if (!font.loadFromFile("D:/Projekt_cpp/gra/Arial_Bold.ttf"))
    {
        printf("Nie mozna wczytac czcionki");
    }
    text.setFont(font);
    text.setCharacterSize(24);
    text.setFillColor(sf::Color::Black);
    text.setPosition(this->x, this->y);
    text.setString("Are you sure you want to exit?\nPress enter to continue or escape\nto go back to pause");

}

void Outro::draw(sf::RenderWindow& window) {
    window.draw(text);
}

class Intro {
private:
    int x;
    int y;
    sf::Text text;
    sf::Font font;
public:
    Intro(int x, int y);
    void draw(sf::RenderWindow& window);
};

Intro::Intro(int x, int y) {
    this->x = x;
    this->y = y;
    if (!font.loadFromFile("D:/Projekt_cpp/gra/Arial_Bold.ttf"))
    {
        printf("Nie mozna wczytac czcionki");
    }
    text.setFont(font);
    text.setCharacterSize(24);
    text.setFillColor(sf::Color::Black);
    text.setPosition(this->x, this->y);
    text.setString("Control the dragon with arrow keys, \nshoot fireballs with SPACE.\nAvoid contact with enemies \nand collect diamonds for hearts.\nYou can shoot only one fireball at the time");

}

void Intro::draw(sf::RenderWindow& window) {
    window.draw(text);
}
class Pause {
private:
    int x;
    int y;
    sf::Text text;
    sf::Font font;
public:
    Pause(int x, int y);
    void draw(sf::RenderWindow& window, int pointing, bool options, bool game_mode, bool skin, bool saving);
    void update(int pointing);
};

Pause::Pause(int x, int y) {
    if (!font.loadFromFile("D:/Projekt_cpp/gra/Arial_Bold.ttf"))
    {
        printf("Nie mozna wczytac czcionki");
    }
    text.setFont(font);
    text.setCharacterSize(30);
    text.setFillColor(sf::Color::Red);
    text.setPosition(x, y);
    text.setString("Game Over");
}

void Pause::draw(sf::RenderWindow& window, int pointing, bool options, bool game_mode, bool skin, bool saving) {
    if (options == false && saving == false) {
        if (pointing == 0) {
            text.setFillColor(sf::Color(100, 0, 255));
        }
        else {
            text.setFillColor(sf::Color(255, 255, 255));
        }
        text.setPosition(300, 100);
        text.setString("Resume");
        window.draw(text);
        if (pointing == 1) {
            text.setFillColor(sf::Color(100, 0, 255));
        }
        else {
            text.setFillColor(sf::Color(255, 255, 255));
        }
        text.setPosition(300, 200);
        text.setString("Options");
        window.draw(text);
        if (pointing == 2) {
            text.setFillColor(sf::Color(100, 0, 255));
        }
        else {
            text.setFillColor(sf::Color(255, 255, 255));
        }
        text.setPosition(300, 300);
        text.setString("Exit");
        window.draw(text);
        if (pointing == 3) {
            text.setFillColor(sf::Color(100, 0, 255));
        }
        else {
            text.setFillColor(sf::Color(255, 255, 255));
        }
        text.setPosition(300, 400);
        text.setString("Save");
        window.draw(text);
    }
    else if (saving == true) {
        text.setPosition(300, 100);
        text.setString("Type your nickname to \nsave high score:");
        window.draw(text);
    }
    else {
        if (game_mode == false && skin == false) {
            if (pointing == 0) {
                text.setFillColor(sf::Color(100, 0, 255));
            }
            else {
                text.setFillColor(sf::Color(255, 255, 255));
            }
            text.setPosition(300, 100);
            text.setString("Change skin");
            window.draw(text);
            if (pointing == 1) {
                text.setFillColor(sf::Color(100, 0, 255));
            }
            else {
                text.setFillColor(sf::Color(255, 255, 255));
            }
            text.setPosition(300, 250);
            text.setString("Game difficulty");
            window.draw(text);
        }
        else {
            if (game_mode == true) {
                if (pointing == 0) {
                    text.setFillColor(sf::Color(100, 0, 255));
                }
                else {
                    text.setFillColor(sf::Color(255, 255, 255));
                }
                text.setPosition(300, 100);
                text.setString("Easy");
                window.draw(text);
                if (pointing == 1) {
                    text.setFillColor(sf::Color(100, 0, 255));
                }
                else {
                    text.setFillColor(sf::Color(255, 255, 255));
                }
                text.setPosition(300, 250);
                text.setString("Hard");
                window.draw(text);
            }
            else if (skin == true) {
                if (pointing == 0) {
                    text.setFillColor(sf::Color(100, 0, 255));
                }
                else {
                    text.setFillColor(sf::Color(255, 255, 255));
                }
                text.setPosition(300, 100);
                text.setString("Yellow dragon");
                window.draw(text);
                if (pointing == 1) {
                    text.setFillColor(sf::Color(100, 0, 255));
                }
                else {
                    text.setFillColor(sf::Color(255, 255, 255));
                }
                text.setPosition(300, 250);
                text.setString("Red Dragon");
                window.draw(text);
            }
        }
    }
}


class GameOver {
private:
    int x;
    int y;
    sf::Text text;
    sf::Font font;
    std::string points;

public:
    GameOver(int x, int y);
    void draw(sf::RenderWindow& window, bool is_game_over);
    void update(int num_of_points);

};

GameOver::GameOver(int x, int y) {
    if (!font.loadFromFile("D:/Projekt_cpp/gra/Arial_Bold.ttf"))
    {
        printf("Nie mozna wczytac czcionki");
    }
    text.setFont(font);

    text.setCharacterSize(30);
    text.setFillColor(sf::Color::Black);
    text.setPosition(x, y);
    text.setString("Game Over");
    this->x = x;
    this->y = y;
}


void GameOver::draw(sf::RenderWindow& window, bool is_game_over) {
    if (is_game_over == true) {
        window.draw(text);
    }
}

class Hearts {
private:
    int x;
    int y;
    int num_of_hearts = 3;
    sf::Texture texture;
    sf::Sprite heart;
public:
    Hearts(int z);
    void update(int hearts);
    void draw(sf::RenderWindow& window);
};

Hearts::Hearts(int z) {
    texture.loadFromFile("D:/Projekt_cpp/gra/Images/heart.png");
    heart.setTexture(texture);

}
void Hearts::draw(sf::RenderWindow& window) {
    for (int i = 1; i <= num_of_hearts; i++) {
        heart.setPosition(1000 - 40 * i, 10);
        window.draw(heart);
    }
}

void Hearts::update(int hearts) {
    num_of_hearts = hearts;
}


class Points {
private:
    sf::Text text;
    sf::Font font;
    std::string points;

public:
    Points(int x, int y);
    void draw(sf::RenderWindow& window);
    void update(int num_of_points);
};

Points::Points(int x, int y) {
    if (!font.loadFromFile("D:/Projekt_cpp/gra/Arial_Bold.ttf"))
    {
        printf("Nie mozna wczytac czcionki");
    }
    text.setFont(font);

    text.setCharacterSize(30);
    text.setFillColor(sf::Color::Black);
    text.setPosition(x, y);
}


void Points::draw(sf::RenderWindow& window) {
    window.draw(text);
}

void Points::update(int num_of_points) {
    points = std::to_string(num_of_points);
    text.setString(points);
}
class Enemy {
private:
    int x;
    int y;
    sf::Texture teksture;
    sf::Sprite enemy;
    float speed_x = 10;
    float speed_y = 1;
    bool easy_mode = true;
    int enemy_type;

public:
    Enemy(int x, int y);
    void update(bool easy_mode);
    void draw(sf::RenderWindow &window);
    sf::Vector2f get_position();
    void set_position(int x, int y);
    sf::Sprite get_sprite();
};

Enemy::Enemy(int x, int y) {
    enemy_type = rand() % 3;
    if (enemy_type == 0) {
        teksture.loadFromFile("D:/Projekt_cpp/gra/Images/enemy0.png");
    }
    else {
        teksture.loadFromFile("D:/Projekt_cpp/gra/Images/enemy1.png");
    }
    enemy.setTexture(teksture);
    if (enemy_type == 0) {
        enemy.setScale(0.5f, 0.5f);
    }
    this->x = x;
    this->y = y;
    enemy.setPosition(this->x, this->y);

}

void Enemy::update(bool easy_mode) {
    if (x > -20) {
        x -= speed_x;
        enemy.move(-speed_x, 0);
    }
    else {
        x = rand() % 500 + 1000;
        y = rand() % 500;
        enemy.setPosition(x, y);
    }
    if (easy_mode == false) {
        speed_x += 0.005;
        
    }
}

void Enemy::draw(sf::RenderWindow &window) {
    window.draw(enemy);
}

sf::Vector2f Enemy::get_position() {
    return enemy.getPosition();
}

void Enemy::set_position(int x, int y) {
    enemy.setPosition(x, y);
}

sf::Sprite Enemy::get_sprite() {
    return enemy;
}

class Dragon {
private:
    int x = 100;
    int y = 250;
    sf::Texture tekstura;
    sf::Sprite dragon;
    bool moving_right = false;
    bool moving_left = false;
    bool moving_up = false;
    bool moving_down = false;
    int speed_x = 10;
    int speed_y = 10;
    static int position[2];

    int frame = 0;
    int counter = 0;

public:
    Dragon(int x);
    void draw(sf::RenderWindow& window);
    void update();
    void move_right();
    void move_left();
    void move_up();
    void move_down();
    int get_x();
    int get_y();
    void update_texture();
    bool check_collision(Enemy enemy);
    sf::Sprite get_sprite();
    void set_position(int x, int y);
    void change_skin(int skin_num);
};

Dragon::Dragon(int z) {
    tekstura.loadFromFile("D:/Projekt_cpp/gra/Images/flying_dragon1.png");
    dragon.setTexture(tekstura);
    dragon.setTextureRect(sf::IntRect(0, 128, 144, 128));
    dragon.setPosition(x, y);
}

void Dragon::draw(sf::RenderWindow& window) {
    window.draw(dragon);
}

void Dragon::update() {
    if (moving_right == true && x < 1000 - 144) {
        dragon.move(speed_x, 0);
        x += speed_x;
    }
    if (moving_left == true && x > 0) {
        dragon.move(-speed_x, 0);
        x -= speed_x;
    }
    if (moving_up == true && y > 0) {
        dragon.move(0, -speed_y);
        y -= speed_y;
    }
    if (moving_down == true && y < 600 - 144) {
        dragon.move(0, speed_y);
        y += speed_y;
    }
    if (y < 600-144) {
        y += 3;
        dragon.move(0, 3);
    }
    moving_right = false;
    moving_down = false;
    moving_left = false;
    moving_up = false;
    update_texture();
}

void Dragon::update_texture() {
    if (counter < 7) {
        counter++;
    }
    else {
        counter = 0;
        dragon.setTextureRect(sf::IntRect(144*frame, 128, 144, 128));
        frame += 1;
        if (frame == 3) {
            frame = 0;
        }
    }
}

void Dragon::move_right() {
    moving_right = true;
}
void Dragon::move_left() {
    moving_left = true;
}
void Dragon::move_up() {
    moving_up = true;
}
void Dragon::move_down() {
    moving_down = true;
}

int Dragon::get_x() {
    return x;
}

int Dragon::get_y() {
    return y;
}

bool Dragon::check_collision(Enemy enemy) {
    sf::Sprite enemy_sprite = enemy.get_sprite();
        if (dragon.getGlobalBounds().intersects(enemy_sprite.getGlobalBounds())) {
            return true;
    }
}

sf::Sprite Dragon::get_sprite() {
    return dragon;
}

void Dragon::set_position(int x, int y) {
    dragon.setPosition(x, y);
    this->x = x;
    this->y = y;
}

void Dragon::change_skin(int skin_num) {
    if (skin_num == 0) {
        tekstura.loadFromFile("D:/Projekt_cpp/gra/Images/flying_dragon1.png");
        dragon.setTexture(tekstura);
    }
    else {
        tekstura.loadFromFile("D:/Projekt_cpp/gra/Images/flying_dragon2.png");
        dragon.setTexture(tekstura);
    }
}

class Fireball {
private:
    int x;
    int y;
    sf::Texture teksture;
    sf::Sprite fireball;
    int frame = 0;
    sf::Clock zegar;
    int speed = 8;
    bool fired = false;
public:
    Fireball(int x, int y);
    void fire(int x, int y);
    void update();
    void draw(sf::RenderWindow& window);
    void check_collision();
    bool check_enemy_collision(Enemy enemy);

};

Fireball::Fireball(int x, int y) {
    this->x = x;
    this->y = y;

    teksture.loadFromFile("D:/Projekt_cpp/gra/Images/fireball_sheet.png");
    fireball.setTexture(teksture);
    fireball.setTextureRect(sf::IntRect(0, 0, 64, 64));
    //fireball.setScale(-64, -64);
    fireball.setPosition(this->x, this->y);
}

void Fireball::draw(sf::RenderWindow& window) {
    window.draw(fireball);
}

void Fireball::update() {
    if (zegar.getElapsedTime().asMilliseconds() > 30.0f) {
        fireball.setTextureRect(sf::IntRect(64 * frame, 0, 64, 64));
        frame += 1;
        if (frame == 5) {
            frame = 0;
        }
        else if (frame == 8) {
            frame = 0;
            fireball.setPosition(-100, 100);
            x = -100;
            fired = false;
        }
        zegar.restart();
    }
    if (fired == true) {
        fireball.move(speed, 0);
        x += speed;
    }
}

void Fireball::fire(int x, int y) {
    if (fired != true) {
        fireball.setPosition(x, y);
        this->x = x;
        this->y = y;
        fired = true;
    }
}

void Fireball::check_collision() {
    if (x >= 1000) {
        fireball.setPosition(-100, 100);
        x = -100;
        fired = false;
    }
}


bool Fireball::check_enemy_collision(Enemy enemy) {
    sf::Sprite enemy_sprite = enemy.get_sprite();
    if (fireball.getGlobalBounds().intersects(enemy_sprite.getGlobalBounds())) {
        frame = 6;
        return true;
    }
}


class Background {
private:
    int x1, y1, x2, y2;
    sf::Texture teksture;
    sf::Sprite bg1;
    sf::Sprite bg2;
    float speed = 4;
public:
    Background(int x);
    void draw(sf::RenderWindow& window);
    bool switch_bg(Background bg2);
    void update(bool easy_mode);
};

Background::Background(int x) {
    x1 = 0;
    y1 = 0;
    x2 = 1024;
    y2 = 0;
    teksture.loadFromFile("D:/Projekt_cpp/gra/Images/sky(1).png");
    bg1.setTexture(teksture);
    bg1.setPosition(x1, y1);
    bg2.setTexture(teksture);
    bg2.setPosition(x2, y2);

}

void Background::draw(sf::RenderWindow& window) {
    window.draw(bg1);
    window.draw(bg2);
}

bool Background::switch_bg(Background bg2) {
    return true;
}

void Background::update(bool easy_mode) {
    if (x1 < -1024) {
        x1 = x2 + 1024;
        bg1.setPosition(x1, y1);
    }
if (x2 < -1024) {
    x2 = x1 + 1024;
    bg2.setPosition(x2, y2);
}
bg1.move(-speed, 0);
bg2.move(-speed, 0);
x1 -= speed;
x2 -= speed;
}

class Diamond {
private:
    int x;
    int y;
    sf::Texture texture;
    sf::Sprite diamond;
    float speed = 7;
public:
    Diamond(int z);
    void draw(sf::RenderWindow& window);
    bool check_collision(Dragon dragon);
    void update(bool easy_mode);
};

Diamond::Diamond(int z) {
    texture.loadFromFile("D:/Projekt_cpp/gra/Images/diamond.png");
    diamond.setTexture(texture);
    diamond.setScale(0.03f, 0.03f);

    int x = 1400;
    int y = rand() % 500;

    diamond.setPosition(x, y);
}

void Diamond::update(bool easy_mode) {
    if (x > -50) {
        x -= speed;
        diamond.move(-speed, 0);
    }
    else {
        x = 1400;
        y = rand() % 500;
        diamond.setPosition(x, y);
    }
    if (easy_mode == false) {
        speed += 0.005;
    }
}

bool Diamond::check_collision(Dragon dragon) {
    sf::Sprite dragon_sprite = dragon.get_sprite();
    if (diamond.getGlobalBounds().intersects(dragon_sprite.getGlobalBounds())) {
        x = 1400;
        y = rand() % 500;
        diamond.setPosition(x, y);
        return true;
    }
}

void Diamond::draw(sf::RenderWindow& window) {
    window.draw(diamond);
}

int main()
{
    srand(time(NULL));

    FILE* fp;
    double buf, tab[5] = { 1, 3, 5, 6, 5 };
    fp = fopen("high_score.dat", "w+b");
    for (int i = 0; i < 5; i++)// Odczyt 5 liczb z pliku
    {
        fwrite(&tab[i], sizeof(double), 1, fp);
    }
    fclose(fp);


    char nick[10];
    int i = 0;

    Points points(800, 500);
    int num_of_points = 0;
    int num_of_hearts = 3;
    int lives = 3;
    bool is_game_over = false;
    bool options = false;
    bool game_mode = false;
    bool is_intro = true;
    bool is_outro = false;
    bool is_saving = false;
    bool skin = false;
    bool easy_mode = false;
    int pause_pointing = 0;

    sf::RenderWindow window(sf::VideoMode(1000, 600), "Dragon game");
    sf::Clock zegar;

    Enemy enemies[2] = { Enemy(800, 500), Enemy(1000, 100) };


    Dragon dragon(3);
    Background background(3);
    Fireball fireball(-100, 100);
    Hearts hearts(3);

    Diamond diamond(3);

    GameOver game_over(300, 300);

    Pause pause(300, 300);
    Intro intro(300, 200);
    Outro outro(300, 200);

    bool is_pause = false;
    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
            if (is_saving == true) {
                if (event.type == sf::Event::TextEntered)
                {
                    if (event.text.unicode < 128 && i < 10 && event.key.code != sf::Keyboard::Enter) {
                        nick[i] = static_cast<char>(event.text.unicode);
                        i++;
                    }
                }
            }
            if (is_pause == true){
                if (event.type == sf::Event::KeyReleased) {

                    if (event.key.code == sf::Keyboard::Key::Up) {
                        pause_pointing -= 1;
                    }
                    if (event.key.code == sf::Keyboard::Key::Down) {
                        pause_pointing += 1;
                    }
                    if (pause_pointing == -1) {
                        pause_pointing = 3;
                    }
                    if (pause_pointing == 4) {
                        pause_pointing = 0;
                    }
                    if (event.key.code == sf::Keyboard::Key::Enter) {
                        if (is_pause == true && options == false && is_outro == false && is_saving == false) {
                            if (pause_pointing == 0) {
                                is_pause = false;
                            }
                            if (pause_pointing == 1) {
                                options = true;
                            }
                            if (pause_pointing == 2) {
                                is_outro = true;
                            }
                            if (pause_pointing == 3) {
                                is_saving = true;
                            }
                        }
                        else if (is_outro == true) {
                            if (is_outro = true) {
                                window.close();
                            }
                        }
                        else if (options == true && skin == false && game_mode == false) {
                            if (pause_pointing == 0) {
                                skin = true;
                            }
                            else if (pause_pointing == 1) {
                                game_mode = true;
                            }
                        }
                        else if (skin == true) {
                            if (pause_pointing == 0) {
                                dragon.change_skin(0);
                            }
                            else if (pause_pointing == 1) {
                                dragon.change_skin(1);
                            }
                            skin = false;
                        }
                        else if (game_mode == true) {
                            if (pause_pointing == 0) {
                                easy_mode = true;
                            }
                            else if (pause_pointing == 1) {
                                easy_mode = false;
                            }
                            game_mode = false;
                        }
                        else if (is_saving == true) {
                            is_saving = false;
                            fp = fopen("nicknames.txt", "a+b");
                            for (int j = 0; j < i; j++) {
                                fwrite(&nick[j], sizeof(char), 1, fp);
                            }
                            fclose(fp);
                            i = 0;

                        }
                        if (is_game_over == true) {
                            is_game_over = false;
                            num_of_points = 0;
                            num_of_hearts = 3;
                            dragon.set_position(100, 300);
                        }

                    }
                }
            }
        }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Left)) {
                dragon.move_left();
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Right)) {
                dragon.move_right();
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Up)) {
                dragon.move_up();
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Down)) {
                dragon.move_down();
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Space)) {
                fireball.fire(dragon.get_x() + 70, dragon.get_y() + 30);
            }

            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Escape)) {
                is_pause = true;

                    options = false;
                    game_mode = false;
                    skin = false;
                    is_saving = false;
                if (is_outro == true) {
                    is_outro = false;
                }
            }
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Enter)) {
                if (is_pause == true && options == false) {
                    if (pause_pointing == 0) {
                        is_pause = false;
                    }
                }
                if (is_game_over == true) {
                    is_game_over = false;
                    num_of_points = 0;
                    num_of_hearts = 3;
                    dragon.set_position(100, 300);
                }
                if (is_intro == true) {
                    is_intro = false;
                }
            }
            if (zegar.getElapsedTime().asMilliseconds() > 16.0f) {
                window.clear();
                if (is_pause != true && is_intro == false) {
                    dragon.update();
                    background.update(easy_mode);
                    fireball.update();
                    hearts.update(num_of_hearts);
                    points.update(num_of_points);
                    diamond.update(easy_mode);
                    for (int i = 0; i < 2; i++) {
                        enemies[i].update(easy_mode);
                    }
                
                    background.draw(window);
                    fireball.draw(window);
                    fireball.check_collision();
                    dragon.draw(window);
                    for (int i = 0; i < 2; i++) {
                        enemies[i].draw(window);
                        if (fireball.check_enemy_collision(enemies[i]) == true) {
                            enemies[i].set_position(-1000, 30);
                            num_of_points += 1000;
                        }
                        else if (dragon.check_collision(enemies[i]) == true) {
                            enemies[i].set_position(-1000, 30);
                            num_of_hearts -= 1;
                            num_of_points -= 500;
                            if (num_of_hearts == 0) {
                                is_pause = true;
                                is_game_over = true;
                            }
                        }
                    }
                    if (diamond.check_collision(dragon) == true) {
                        num_of_hearts += 1;
                    }
                    points.draw(window);
                    hearts.draw(window);
                    diamond.draw(window);
                    game_over.draw(window, is_game_over);
                }
                else if (is_pause == false && is_intro == true) {
                    background.draw(window);
                    intro.draw(window);
                }
                if (is_pause == true) {
                    if (is_outro == false) {
                        pause.draw(window, pause_pointing, options, game_mode, skin, is_saving);
                    }
                    else {
                        background.draw(window);
                        outro.draw(window);
                    }
                }
                zegar.restart();
                window.display();
            }

    }

    return 0;
}