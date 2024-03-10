#include <iostream>
#include <fstream>
#include <string.h>

using namespace std;


enum class pokemon_type{
    ELECTRIC = 1,
    PSYCHO,
    ICE,
    DRAGON,
    DARK,
    FAIRY
};

struct pokemon{
    void show_info();
    int calculate_score();
    void print_info();
    bool is_available(int sum);
    pokemon(string name_, double weight_,
                 pokemon_type type_, int hp_,
                 int damage_, int defence_, int super_attack_,
                 int super_defence_, int speed_);
private:
    string name;
    double weight;
    pokemon_type type;
    int hp;
    int damage;
    int defence;
    int super_attack;
    int super_defence;
    int speed;
};

pokemon::pokemon(string name_, double weight_,
                 pokemon_type type_, int hp_,
                 int damage_, int defence_, int super_attack_,
                 int super_defence_, int speed_){
                    name = name_;
                    weight = weight_;
                    type = type_;
                    hp = hp_;
                    damage = damage_;
                    defence = defence_;
                    super_attack = super_attack_;
                    super_defence = super_defence_;
                    speed = speed_;}

void pokemon::show_info(){
    cout<<"»м€: "<<name<<", вес: "<<weight<<", тип: "<<static_cast<int>(type)\
    <<", здоровье: "<<hp<<", урон: "<<damage<<", защита: "<<defence\
    <<", супер-атака: "<<super_attack<<", супер-защита: "<<super_defence\
    <<", скорость: "<<speed<<"."<<endl;
}

/*
int pokemon::calculate_score(){
    int sum = 0;
    if (weight > 30.0 && weight < 100.0)
        sum += 1;
    if (type == pokemon_type::PSYCHO ||\
        type == pokemon_type::ICE ||\
        type == pokemon_type::FAIRY)
            sum += 1;
    if  (hp >= 50 && hp < 100)
        sum += 1;
    else{ if (hp >= 100)
        sum += 2;
    }
    if  (damage >= 10 && damage <= 30)
        sum += 1;
    else{ if (damage > 30)
        sum += 2;
    }
    if  (defence >= 10 && defence <= 30)
        sum += 1;
    else{ if (defence > 30)
        sum += 2;
    }
    if  (super_attack < 100)
        sum -= 1;
    else{ if (super_attack >= 100 &&\
              super_attack <= 150)
        sum += 1;
            else{ if (super_attack > 150)
                sum += 2;
            }
    }
    if (super_defence < 100)
        sum -= 1;
    else{ if (super_defence >= 100 &&\
              super_defence <= 150)
        sum += 1;
            else{ if (super_defence > 150)
                sum += 2;
            }
    }
    if  (speed >= 10 && speed <= 15){
        sum += 1;}
    else{ if (speed > 15)
        sum += 2;
    return sum;
    }
}
*/

void pokemon::print_info(){
    int sum = 0;
    if (weight > 30.0 && weight < 100.0)
        {cout<<"¬ес +1 балл, ";
        sum += 1;}
    else cout<<"¬ес 0 баллов, ";
    if (type == pokemon_type::PSYCHO ||\
        type == pokemon_type::ICE ||\
        type == pokemon_type::FAIRY)
            {cout<<"тип +1 балл, ";
            sum += 1;}
    else cout<<"тип 0 баллов, ";
    if  (hp >= 50 && hp < 100)
        {cout<<"хп +1 балл, ";
        sum += 1;}
    else{ if (hp >= 100)
        {cout<<"хп +2 балла, ";
        sum += 2;}
        else{
            cout<<"хп 0 баллов, ";
        }
    }
    if  (damage >= 10 && damage <= 30)
        {cout<<"урон +1 балл, ";
        sum += 1;}
    else{ if (damage > 30)
        {cout<<"урон +2 балла, ";
        sum += 2;}
        else{
            cout<<"урон 0 баллов, ";
        }
    }
    if  (defence >= 10 && defence <= 30)
        {cout<<"защита +1 балл, ";
        sum += 1;}
    else{ if (defence > 30)
        {cout<<"защита +2 балла, ";
        sum += 2;}
        else{
            cout<<"защита 0 баллов, ";
        }
    }
    if  (super_attack < 100)
        {cout<<"супер-атака -1 балл, ";
        sum -= 1;}
    else{ if (super_attack >= 100 &&\
              super_attack <= 150)
        {cout<<"супер-атака +1 балл, ";
        sum += 1;}
            else{ if (super_attack > 150)
                {cout<<"супер-атака +2 балла, ";
                sum += 2;}
            }
    }
    if (super_defence < 100)
        {cout<<"супер-защита -1 балл, ";
        sum -= 1;}
    else{ if (super_defence >= 100 &&\
              super_defence <= 150)
        {cout<<"супер-защита +1 балл, ";
        sum += 1;}
            else{ if (super_defence > 150)
                {cout<<"супер-защита +2 балла, ";
                sum += 2;}
            }
    }
    if  (speed >= 10 && speed <= 15)
        {cout<<"скорость +1 балл = ";
        sum += 1;}
    else{ if (speed > 15)
        {cout<<"скорость +2 балла = ";
        sum += 2;}
        else{
            cout<<"скорость 0 баллов = ";
        }
    }
    cout<<sum<<"."<<endl;
    if (is_available(sum)){
        cout<<"ƒопущен.";
    }
    else{
        cout<<"Ќе допущен.";
    }
    cout<<endl;
}

bool pokemon::is_available(int sum){
    return (sum >= 10);
    }

int main()
{
    setlocale(LC_ALL, "Russian");
    pokemon* pokemons[100];
    string data;
    ifstream in("C:\\Users\\semyo\\Desktop\\in.txt");
    int elem = 0;
    while (getline(in, data)){
        string name;
        double weight;
        string type_prom;
        pokemon_type type;
        int hp;
        int damage;
        int defence;
        int super_attack;
        int super_defence;
        int speed;
        char buff[255];
        strcpy(buff, data.c_str());
        char *tmp_char;
        tmp_char = strtok(buff, " ");
        int cnt = 0;
        while (tmp_char != NULL){
            //cout<<tmp_char<<" "<<cnt<<endl;
            switch (cnt){
                case 0: name = tmp_char;
                break;
                case 1: weight = atof(tmp_char);
                break;
                case 2: type_prom = tmp_char;
                break;
                case 3: hp = atoi(tmp_char);
                break;
                case 4: damage = atoi(tmp_char);
                break;
                case 5: defence = atoi(tmp_char);
                break;
                case 6: super_attack = atoi(tmp_char);
                break;
                case 7: super_defence = atoi(tmp_char);
                break;
                case 8: speed = atoi(tmp_char);
            }
            tmp_char = strtok(NULL, " ");
            cnt += 1;
        }
        if (type_prom == "ELECTRIC"){
            type = pokemon_type::ELECTRIC;
        }
        if (type_prom == "PSYCHO"){
            type = pokemon_type::PSYCHO;
        }
        if (type_prom == "ICE"){
            type = pokemon_type::ICE;
        }
        if (type_prom == "DRAGON"){
            type = pokemon_type::DRAGON;
        }
        if (type_prom == "DARK"){
            type = pokemon_type::DARK;
        }
        if (type_prom == "FAIRY"){
            type = pokemon_type::FAIRY;
        }
        pokemon *p = new pokemon(name, weight, type, hp, damage,\
                                defence, super_attack, super_defence, speed);
        pokemons[elem] = p;
        elem += 1;
    }
    for (int i = 0; i < elem; i++){
        pokemons[i]->show_info();
        pokemons[i]->print_info();
        /*
        if (pokemons[i]->is_available(pokemons[i]->calculate_score()))
            cout<<"ƒопущен";
        else{
            cout<<"Ќе допущен";
        }*/
        cout<<endl;
    }
    in.close();
}
