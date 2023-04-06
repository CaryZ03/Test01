package com.example.demo.Service;

import com.example.demo.Entity.Student;
import org.springframework.stereotype.Service;

@Service
public interface StudentService {
    public Student selectStudentByUsername(String username);
    public void registerNewStudent(Student student);
    public Student showStudent(String username);
}
