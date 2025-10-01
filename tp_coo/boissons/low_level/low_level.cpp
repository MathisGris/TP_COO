#include <iostream>
#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>     

class Localisation {
    public:
        Localisation() {}
        Localisation(const std::string& nom, const std::string& taxes, float prix_m2) : nom{nom}, taxes{taxes}, prix_m2{prix_m2} {}

        std::string nom;
        float prix_m2;
        std::string taxes;
        
        auto affichage() {std::cout << "Nom :" << nom << "\nTaxes :" << taxes << "\nprix :" << prix_m2 << "euros au m2";}
};

auto main() -> int {
    auto localisation = Localisation{"Courchevel", "20%", 5000};
    localisation.affichage();
    cpr::Response patate = cpr::Get(cpr::Url{"http://localhost:8000/localisation/1"});

    std::cout << "\n" << patate.text;

    nlohmann::json data = nlohmann::json::parse(patate.text);

    std::string nom = data["nom"];
    std::string taxes_str = data["taxes"];
    double prix_m2 = data["prix_m2"];

    std::cout << "Nom     : " << nom << "\n";
    std::cout << "Taxes   : " << taxes_str << "\n";
    std::cout << "Prix m2 : " << prix_m2 << "\n";

    return 0;
}