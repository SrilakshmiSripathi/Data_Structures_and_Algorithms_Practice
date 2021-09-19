def nextClosestTime(time):
        """
        :type time: str
        :rtype: str
        """
        try:
            if len(time) == 5:
                digits = set(digit for digit in time.replace(":",""))
                hour, minute = time.split(":")
            else:
                return "Invalid time"
        
            while True:
                # Increment by one minute + handle minute 59 overflow
                if minute == '59':
                    hour = str(int(hour) + 1)
                    minute = '00'
                else:
                    minute = str(int(minute) + 1)
            
                # Fix hour overflow from 23 -> 00
                if int(hour) > 23:
                    hour = '00'
                
                # Fill digits with zero
                if len(hour) == 1:
                    hour = '0' + hour
                if len(minute) == 1:
                    minute = '0' + minute
                    
                if all(x in digits for x in hour + minute):
                    return hour + ':' + minute
        except ValueError:
            return "Invalid time"


print nextClosestTime("13:33")
