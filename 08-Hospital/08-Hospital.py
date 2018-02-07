class Patient(object):
    def __init__(self, uid=None, name=None, allergie=None, bed_num=None):
        self.uid = uid
        self.name = name
        self.allergie = allergie
        if bed_num == None:
            self.bed_num = 0
        else:
            self.bed_num = bed_num

class Hospital(Patient):
    def __init__(self, hospital_name, capacity):
        super(Hospital, self).__init__()
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.patient = []
        self.total_patient = 0
    def admit(self, patients):
        if self.total_patient + 1 > self.capacity:
            print "* This {} hospital is full.".format(self.hospital_name)
            print "  Please take patient {} to another hospital.".format(patients.name)
            return self
        self.patient.append(patients)
        self.total_patient = len(self.patient)
        return self
    def info(self):
        print "** {} hospital with capacity of {}.".format(self.hospital_name, self.capacity)
        print "   Current total of patients is {}".format(self.total_patient)
        for x in range(self.total_patient):
            print "Patient ID: {}".format(self.patient[x].uid)
            print "Patient Name: {}".format(self.patient[x].name)
            print "Patient Allergies: {}".format(self.patient[x].allergie)
            print "Patient Bed Number: {}".format(self.patient[x].bed_num)
        return self
    def discharge(self, name):
        print "* Searching"
        idx = -1
        for x in range(0,self.total_patient):
            if self.patient[x].name == name:
                print "Found patient {} at {}".format(self.patient[x].name, x)
                idx = x
        if idx >= 0:
            print "Patient {} is discharged from the hopistal!".format(self.patient[idx].name)
            self.patient.pop(idx)
            self.total_patient = len(self.patient)
        else:
            print "Patient {} not found in the hopistal!".format(name)
        return self

print "----->"
x = Hospital("OU", 3)
x.info()
x.admit(Patient(1,"Alex","fever",101))
x.admit(Patient(2,"Bob","fever",102))
x.admit(Patient(3,"Tom","fever",103))
x.info()
print "----->"
x.admit(Patient(3,"John","fever"))
print "----->"
x.discharge('Bobby').info()
print "----->"
x.discharge('Bob').info()
