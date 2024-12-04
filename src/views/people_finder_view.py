import os
from typing import Dict


class PeopleFinderView:
    def find_person_view(self) -> Dict:
        os.system('cls||clear')

        print('Buscar Pessoa \n\n')
        name = input('Nome:')

        person_finder_informations = {
            "name": name
        }

        return person_finder_informations
    
    def find_person_success(self, message: Dict) -> None:
        os.system('cls||clear')

        success_message = f"""
            Usuário encontrado com sucesso!

            Tipo {message['type']}
            Registros: {message['count']}
            Infos: :
                Nome: {message['infos']['name']}
                Age: {message['infos']['age']}
                Height: {message['infos']['height']}
        """
        print(success_message)

    def find_person_error(self, message: Dict) -> None:

        error_message = f"""
            Falha ao buscar usuário!
            
            Erro: {message['error']}
        """