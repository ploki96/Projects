package com.timothywang.beltExam.services;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import com.timothywang.beltExam.models.Student;
import com.timothywang.beltExam.repositories.StudentRepository;



@Service
public class StudentService {
	private final StudentRepository repo;
	
	public StudentService(StudentRepository repo) {
		this.repo = repo;
	}
	
	public List<Student> allStudents() {
		return repo.findAll();
	}
	
	public Student createStudent(Student student) {
		return repo.save(student);
	}
	
	public Student findStudent(Long id) {
		Optional<Student> optionalStudent = repo.findById(id);
		if(optionalStudent.isPresent()) {
			return optionalStudent.get();
		}
		else {
			return null;
		}
	}
	
	public Student updateStudent(Student student) {
		return this.repo.save(student);
	}
}
