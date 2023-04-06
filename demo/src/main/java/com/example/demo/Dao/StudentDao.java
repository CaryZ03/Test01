package com.example.demo.Dao;

import com.example.demo.Entity.Student;
import org.apache.ibatis.annotations.Mapper;

@Mapper
public interface StudentDao {
    public Student selectStudentByUsername(String username);
    public void registerNewStudent(Student student);
    public Student showStudent(String username);
}
