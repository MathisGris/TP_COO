#include <iostream>
#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>     

class Localisation {
    public:
        Localisation() {}
        Localisation(const std::string& nom, const std::string& taxes, float prix_m2) : nom{nom}, taxes{taxes}, prix_m2{prix_m2} {}
        Localisation(nlohmann::json data) : nom{data["nom"]}, taxes{data["taxes"]}, prix_m2{data["prix_m2"]} {}
        Localisation(int id) {
            std::string str_id = std::to_string(id);
            cpr::Response patate = cpr::Get(cpr::Url{"http://localhost:8000/localisation/"+str_id});
            nlohmann::json data = nlohmann::json::parse(patate.text);
            nom = data["nom"];
            taxes = data["taxes"];
            prix_m2 = data["prix_m2"];    
        }

        std::string nom;
        float prix_m2;
        std::string taxes;
        
        auto affichage() {std::cout << "\nNom :" << nom << "\nTaxes :" << taxes << "\nprix :" << prix_m2 << "euros au m2";}
};

class Local {
    public:
        Local() {}
        Local(const std::string& nom, const std::string& taxes, float prix_m2) : nom{nom}, taxes{taxes}, prix_m2{prix_m2} {}
        Local(nlohmann::json data) : nom{data["nom"]}, taxes{data["taxes"]}, prix_m2{data["prix_m2"]} {}
        Local(int id) {
            std::string str_id = std::to_string(id);
            cpr::Response patate = cpr::Get(cpr::Url{"http://localhost:8000/localisation/"+str_id});
            nlohmann::json data = nlohmann::json::parse(patate.text);
            nom = data["nom"];
            localisation = data["localisation"];
            surface = data["surface"];    
        }

        std::string nom;
        std::unique_ptr<> localisation
        float surface;
        
        auto affichage() {std::cout << "\nNom :" << nom << "\nLocalisation :" << localisation << "\nsurface :" << surface << "m2";}
};











auto main() -> int {
    auto localisation = Localisation{"Courchevel", "20%", 5000};
    localisation.affichage();
    cpr::Response patate = cpr::Get(cpr::Url{"http://localhost:8000/localisation/1"});

    std::cout << "\n" << patate.text;

    nlohmann::json data = nlohmann::json::parse(patate.text);

    auto lieu = Localisation{1};
    lieu.affichage();



    return 0;
}