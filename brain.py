from datetime import datetime


weekday = datetime.now().weekday()

current_time = datetime.now().strftime("%H:%M")





match weekday : 
    
    case 0 :
        weekday ="MONDAY"
    case 1 :
        weekday ="TUESDAY"
    case 2 :
        weekday ="WEDNESDAY"
    case 3 :
        weekday ="THURUSDAY"
    case 4 :
        weekday ="FRIDAY"
    case _ :
        weekday ="HOLIDAY"




