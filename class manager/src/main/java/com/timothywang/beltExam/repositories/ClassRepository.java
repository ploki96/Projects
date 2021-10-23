package com.timothywang.beltExam.repositories;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import com.timothywang.beltExam.models.Class;

@Repository
public interface ClassRepository extends CrudRepository<Class, Long>{
	List<Class> findAll();;
	

}