package com.example.demo.Controller;

import com.example.demo.Entity.Student;
import com.example.demo.Service.StudentService;
import com.fasterxml.jackson.databind.node.JsonNodeType;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;

@RestController
public class StudentController {
    @Autowired
    private StudentService studentService;
    @PostMapping("/register")
    public Map<String, Object> register(@RequestBody Map<String, String> re_map) {
        String username = re_map.get("username");
        String password = re_map.get("password");
        Map<String, Object> map = new HashMap<>();
        try {
            Student student1 = studentService.selectStudentByUsername(username);
            if (student1 != null) {
                map.put("success", false);
                map.put("message", "用户名已注册");
            }
            else {
                Student student = new Student(username, password);
                studentService.registerNewStudent(student);
                map.put("success", true);
                map.put("message", "用户注册成功！");
            }
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success", false);
            map.put("message", "用户注册失败");
        }
        return map;
    }
    @PostMapping("/show_info")
    public Map<String, String> show_info(@RequestBody Map<String, String> re_map) {
        String find_username = re_map.get("username");
        Map<String, String> map = new HashMap<>();
        try {
            Student student1 = studentService.showStudent(find_username);
            if (student1 != null) {
                map.put("password", student1.getPassword());
                map.put("username", student1.getUsername());
            }
            else {
                map.put("success", "false");
                map.put("message", "用户名不存在");
            }
        } catch (Exception e) {
            e.printStackTrace();
            map.put("success", "false");
            map.put("message", "未知错误，查询失败");
        }
        return map;
    }
}
