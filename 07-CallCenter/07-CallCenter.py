# import operator

class Call(object):
    def __init__(self, uid, name, phone_number, time_call, reason_call):
        self.uid = uid
        self.name = name
        self.phone_number = phone_number
        self.time_call = time_call
        self.reason_call = reason_call
    def display_info(self):
        print "** Call"
        print "Unique ID: {}".format(self.uid)
        print "Caller Name: {}".format(self.name)
        print "Call Phone Number: {}".format(self.phone_number)
        print "Time of Call: {}".format(self.time_call)
        print "Reasonfor Call: {}".format(self.reason_call)
        return self

class CallCenter(object):
    def __init__(self, calls=None):
        if calls == None:
            self.calls = []
            self.queue_size = 0
        else:
            self.calls = calls
            self.queue_size = len(self.calls)
    def add(self, calls):
        self.calls.append(calls)
        self.queue_size = len(self.calls)
        return self
    def info(self):
        print "** CallCenter"
        print "Current Queue: {}".format(self.queue_size)
        for cc in range(0,self.queue_size):
            print "  Caller Name: {}".format(self.calls[cc].name)
            print "  Call Phone Number: {}".format(self.calls[cc].phone_number)
            print "  Call Time: {}".format(self.calls[cc].time_call)
        return self
    def remove(self):
        print "* Removed"
        self.calls.pop(0)
        self.queue_size = len(self.calls, key=self.uid)
        return self

# print "----->"
# call0 = Call(1,"Alex","123-1111","9.00pm","Burglary").display_info()
# call1 = Call(2,"Tom","123-2222","10.00pm","Burglary").display_info()
# call2 = Call(3,"Sue","123-3333","09.40pm","Burglary").display_info()
# print "----->"
# callcenter = CallCenter()
# callcenter.add(call0).add(call1).add(call2)
# callcenter.info()
# callcenter.remove()
# callcenter.info()

class Ninja(CallCenter):
    def __init__(self):
        super(Ninja, self).__init__()
    def remove_by_phone(self, phone):
        print "* Remove by phone"
        for cc in range(0,self.queue_size):
            if self.calls[cc].phone_number == phone:
                print "Found index={}".format(cc)
                break
        self.calls.pop(cc)
        self.queue_size = len(self.calls)
        return self

# print "----->"
# callcenter = Ninja()
# callcenter.add(Call(1,"Alex","123-1111","9.00pm","Burglary"))
# callcenter.add(Call(2,"Tom","123-2222","10.00pm","Burglary"))
# callcenter.add(Call(3,"Sue","123-3333","09.40pm","Burglary"))
# callcenter.add(Call(4,"Susan","123-4444","10.40pm","Burglary"))
# callcenter.info()
# callcenter.remove_by_phone('123-2222')
# callcenter.info()

class Hacker(CallCenter):
    def __init__(self):
        super(Hacker, self).__init__()
    def sort_by_time(self):
        print "* Sort by Time (selection_sort)"
        # sorted(self.calls, key=operator.attrgetter('uid'))
        for step1 in range(0, self.queue_size):
            smallest = step1
            for step2 in range(step1, self.queue_size):
                if self.calls[step2].time_call < self.calls[smallest].time_call:
                    smallest = step2
            temp_call = self.calls[step1]
            self.calls[step1] = self.calls[smallest]
            self.calls[smallest] = temp_call
        return self

print "----->"
callcenter = Hacker()
callcenter.add(Call(1,"Alex","123-1111","09.00pm","Burglary"))
callcenter.add(Call(2,"Tom","123-2222","10.00pm","Burglary"))
callcenter.add(Call(3,"Sue","123-3333","09.40pm","Burglary"))
callcenter.add(Call(4,"Susan","123-4444","10.40pm","Burglary"))
callcenter.info()
callcenter.sort_by_time()
callcenter.info()
