from datetime import datetime

now = datetime.now()

class TraduccionEspanol:
    def Dia():
        if now.strftime("%A") == "Monday":
            return "Lunes"
        elif now.strftime("%A") == "Tuesday":
            return "Martes"
        elif now.strftime("%A") == "Wednesday":
            return "Miercoles"
        elif now.strftime("%A") == "Thursday":
            return "Jueves"
        elif now.strftime("%A") == "Friday":
            return "Viernes"
        elif now.strftime("%A") == "Saturday":
            return "Sabado"
        elif now.strftime("%A") == "Sunday":
            return "Domingo"

    def Mes():
        if now.strftime("%m") == "1":
            return "Enero"
        elif now.strftime("%m") == "2":
            return "Febrero"
        elif now.strftime("%m") == "3":
            return "Marzo"
        elif now.strftime("%m") == "4":
            return "Abril"
        elif now.strftime("%m") == "5":
            return "Mayo"
        elif now.strftime("%m") == "6":
            return "Junio"
        elif now.strftime("%m") == "7":
            return "Julio"
        elif now.strftime("%m") == "8":
            return "Agosto"
        elif now.strftime("%m") == "9":
            return "Septiembre"
        elif now.strftime("%m") == "10":
            return "Octubre"
        elif now.strftime("%m") == "11":
            return "Noviembre"
        elif now.strftime("%m") == "12":
            return "Diciembre"
