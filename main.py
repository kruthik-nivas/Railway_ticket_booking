from passesnge import Passenger

class App:

    def __init__(self):
        self.ctickets=63
        self.lowerBirths=21
        self.middleBirths=21
        self.upperBirths=21
        self.racTcikets=18
        self.waitingList=10
        self.id=0
        self.li=0
        self.mi=0
        self.ui=0
        self.cancelobj=''
        self.passengers=[]
        self.cpassengers=[]
        self.racpassesngers=[]
        self.waitingListpassengers=[]
    
    def collectDetails(self):
        name = input('Enter your name: ')
        age=int(input('Enter your age: '))
        if age<=5:
            return 0
        gender=input('What is your gender (M,F,O): ')
        preference = input('Enter your birth preference (L,M,U): ')
        self.id+=1
        p = Passenger(self.id,name,age,gender,preference)
        self.passengers.append(p)
        return p
    
    def allocation(self,p):
        l=self.lowerBirths
        m=self.middleBirths
        u=self.upperBirths
        pref = p.preference.lower()
        if self.ctickets>0:
            if pref=='l' and l>0:
                print('Preferred Birth allocated')
                print('\tLower Birth is Booked Sucessfully!')
                self.li+=1
                self.lowerBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.li}L'
                self.cpassengers.append(p)
            elif pref=='m' and m>0:
                print('Preferred Birth allocated')
                print('\tmiddle Birth is Booked Sucessfully!')
                self.mi+=1
                self.middleBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.mi}M'
                self.cpassengers.append(p)
            elif pref=='u' and u>0:
                print('Preferred Birth allocated')
                print('\tupper Birth is Booked Sucessfully!')
                self.ui+=1
                self.upperBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.ui}U'
                self.cpassengers.append(p)
            elif l>0:
                print('Prefered seat Not Available')
                print('\tLower Birth Booked Sucessfully')
                self.li+=1
                self.lowerBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.li}L'
                self.cpassengers.append(p)
            elif m>0:
                print('Prefered seat Not Available')
                print('\tMiddle Birth Booked Sucessfully')
                self.mi+=1
                self.middleBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.mi}M'
                self.cpassengers.append(p)
            elif u>0:
                print('Prefered seat Not Available')
                print('\tUpper Birth Booked Sucessfully')
                self.ui+=1
                self.upperBirths-=1
                self.ctickets-=1
                p.status='confirmed'
                p.seat=f'{self.ui}U'
                self.cpassengers.append(p)
        elif self.racTcikets>0:
            print('Confirmed Seats Not available')
            print('\tRAC Ticket booked succesfully')
            self.racTcikets-=1
            p.status="RAC"
            self.racpassesngers.append(p)
        elif self.waitingList>0:
            print('Only waiting List ticket is available')
            print('\tWaiting list ticket booked sucessfully')
            self.waitingList-=1
            p.status="Waiting"
            self.waitingListpassengers.append(p)
        else:
            print("\tNone of the category tciket is available")
            print('\tSorry for the incovinience')
            return
    
    def findingCustomer(self,id):
        if len(self.passengers)==0:
            return 0
        else:
            for i in self.cpassengers:
                if i.customerId == id:
                    return i
            for i in self.racpassesngers:
                if i.customerId==id:
                    self.cancelobj=i
                    return 2
            for i in self.waitingListpassengers:
                if i.customerId==id:
                    self.cancelobj=i
                    return 3
            else:
                return 0

    def cancelation(self,p):
        self.passengers.remove(p)
        self.cpassengers.remove(p)
        self.ctickets+=1
        berth = p.seat[1].lower()
        seat=p.seat
        if berth=='l':
            self.li-=1
            self.lowerBirths+=1
        elif berth=='m':
            self.mi-=1
            self.middleBirths+=1
        elif berth=='u':
            self.ui-=1
            self.upperBirths+=1
        print(f"Customer Id -> {p.customerId} --> Ticket Cancelled Sucessfully")
        if len(self.racpassesngers)>0:
            print('--'*60)
            rp=self.racpassesngers.pop(0)
            self.allocation(rp)
            rp.seat=seat
            print('Changes made sucessfully in Rac Tickets')
            print('--'*60)
        if len(self.waitingListpassengers)>0:
            print('--'*60)
            wl=self.waitingListpassengers.pop(0)
            self.allocation(wl)
            print("Changes made sucessfully in Waiting List Tickets")
            print('--'*60)

    def availableTickets(self):
        print(f'Lower Births available  -> {self.lowerBirths}')
        print(f'Middle Births available -> {self.middleBirths}')
        print(f'Upper Births available  -> {self.upperBirths}')
        print(f'Rac Tickets available   -> {self.racTcikets}')
        print(f'Waiting List available  -> {self.waitingList}')
    
    def printBookedTickets(self):
        if len(self.passengers)==0:
            print('--'*60)
            print("No Passesngers yet")
            print('--'*60)
        else:    
            for cp in self.passengers:
                print('--'*60)
                cp.printTickets()
                print('--'*60)

    def runApp(self):
        while True:
            print('Enter 1 -> Booking')
            print('Enter 2 -> Cancel Ticket')
            print('Enter 3 -> Available Tickets')
            print('Enter 4 -> Booked Tickets')
            print('Enter 5 -> Exit')
            choice = int(input('Enter your choice: '))
            if choice==1:
                print('--'*60)
                if (self.ctickets+self.racTcikets+self.waitingList)>0:
                    p=self.collectDetails()
                    if p==0:
                        print("No booking required for 5 or less year old child")
                        print('--'*60)
                    else:
                        print('--'*60)
                        print(f'Cutomer Id -> {p.customerId}')
                        self.allocation(p)
                        print('--'*60)
                else:
                    print('No Tickets available')
                    print('--'*60)
            elif choice==2:
                print('--'*60)
                cid=int(input('Enter Customer Id: '))
                p=self.findingCustomer(cid)
                if p==0:
                    print('No Such Customer Found')
                elif p==2:
                    self.racTcikets-=1
                    self.racpassesngers.remove(self.cancelobj)
                    self.passengers.remove(self.cancelobj)
                elif p==3:
                    self.waitingList-=1
                    self.waitingListpassengers.remove(self.cancelobj)
                    self.passengers.remove(self.cancelobj)
                else:
                    self.cancelation(p)
                print('--'*60)
            elif choice==3:
                print('--'*60)
                self.availableTickets()
                print('--'*60)
            elif choice==4:
                self.printBookedTickets()
            elif choice==5:
                print('--'*60)
                print("\t\t\tTravelling teaches a lot")
                print("\t\t\t Thank You visit again!")
                print('--'*60)
                break
    
    
if __name__=='__main__':
    app = App()
    app.runApp()
