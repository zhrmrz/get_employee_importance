class Sol:
    def get_employee_importance(self,employees,id):
        for i in range(len(employees)):
            if employees[i][0]==id:
                self.sub_emp=employees[i][2]
                return employees[i][1]
    def total_importance(self,employees,id):
        val=self.get_employee_importance(employees,id)
        for id in self.sub_emp:
            val+=self.get_employee_importance(employees,id)
        return val

if __name__ == '__main__':
    p=Sol()
    print(p.total_importance([[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1))
