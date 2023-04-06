package com.example.demo.Service.Lmpl;

import com.example.demo.Dao.StudentDao;
import com.example.demo.Entity.Student;
import com.example.demo.Service.StudentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class StudentServiceLmpl implements StudentService {
    private StudentDao studentDao;
    @Override
    public Student selectStudentByUsername(String username) {
        return studentDao.selectStudentByUsername(username);
    }
    public void registerNewStudent(Student student) {
        studentDao.registerNewStudent(student);
    }
    public Student showStudent(String username) {
        return studentDao.showStudent(username);
    }
}
