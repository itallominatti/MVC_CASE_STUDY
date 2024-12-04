from typing import Dict

class PeopleRegisterController:
    def register(self, new_person_informations: Dict) -> Dict:
        try:
            self.__validate_fields(new_person_informations)
            response = self.__format_response(new_person_informations)
            return {
                "success": True,
                "message": response
            }
        except Exception as exception:
            return {
                "success": False,
                "error": str(exception)
            }

    def __validate_fields(self, new_person_informations: Dict) -> None:
        if not isinstance(new_person_informations['name'], str):
            raise Exception('Campo Nome Incorreto!')
        
        try: int(new_person_informations['age'])
        except: raise Exception('Campo Idade Incorreto!')

        try: int(new_person_informations['height']) \
            or float(new_person_informations['height'])
        except: raise Exception('Campo Altura Incorreto!')

    def __format_response(self, new_person_informations: Dict) -> Dict:
        return {
            "count": 1,
            "type": "person",
            "attributes": new_person_informations
        }