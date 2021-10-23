package com.timothywang.beltExam.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;

import com.timothywang.beltExam.models.Student;


public interface StudentRepository extends CrudRepository<Student, Long>{
	List<Student> findAll();
}