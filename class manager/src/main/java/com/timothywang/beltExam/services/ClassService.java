package com.timothywang.beltExam.services;

//import java.sql.Time;
import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.timothywang.beltExam.models.Class;
import com.timothywang.beltExam.repositories.ClassRepository;


@Service
public class ClassService {
    
	@Autowired
	private ClassRepository classRepository;
	
	
	public List<Class> allclasss() {
		return classRepository.findAll();
	}
	
	public Class createClass(Class classe) {
		
		return classRepository.save(classe);
	}
	
	public Class findClass(Long id) {
		Optional<Class> optionalClass = classRepository.findById(id);
		if(optionalClass.isPresent()) {
			return optionalClass.get();
		}
		else {
			return null;
		}
	}
	public Class editClass(Long id, String name, String weekday, Integer price, String time, String description) {
    	Class classe = findClass(id);
    	
    	classe.setName(name);
    	classe.setWeekday(weekday);
    	classe.setPrice(price);
    	classe.setTime(time);
    	classe.setDescription(description);
    	classRepository.save(classe);
    	return classe;
    }
	
	public void deleteClass(Long id) {
    	classRepository.deleteById(id);
    }
	
	public Class updateClass(Class classe) {
		return this.classRepository.save(classe);
	}
}
