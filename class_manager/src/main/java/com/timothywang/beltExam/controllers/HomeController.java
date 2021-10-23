package com.timothywang.beltExam.controllers;

import java.util.List;

import javax.servlet.http.HttpSession;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import com.timothywang.beltExam.models.Class;
import com.timothywang.beltExam.models.LoginUser;
import com.timothywang.beltExam.models.Student;
import com.timothywang.beltExam.models.User;
import com.timothywang.beltExam.services.ClassService;
import com.timothywang.beltExam.services.UserService;
import com.timothywang.beltExam.services.StudentService;




@Controller
public class HomeController {
	@Autowired
    private UserService userServ;
	@Autowired
    private ClassService classServ;
	@Autowired
	private StudentService studentServ;
    
    @GetMapping("/")
    public String index(Model model) {
        model.addAttribute("newUser", new User());
        model.addAttribute("newLogin", new LoginUser());
        return "index.jsp";
    }
    
    @GetMapping("/home")
    public String home(Model model, HttpSession session) {
    	List<Class> classes = classServ.allclasss();
    	model.addAttribute("user", userServ.findUser((Long) session.getAttribute("user_id")));
    	model.addAttribute("classes", classes);
    	return "home.jsp";
    }
    
    @PostMapping("/register")
    public String register(@Valid @ModelAttribute("newUser") User newUser, 
            BindingResult result, Model model, HttpSession session) {
        userServ.register(newUser, result);
        if(result.hasErrors()) {
            model.addAttribute("newLogin", new LoginUser());
            return "index.jsp";
        }
        session.setAttribute("user_id", newUser.getId());
        return "redirect:/home";
    }
    
    @PostMapping("/login")
    public String login(@Valid @ModelAttribute("newLogin") LoginUser newLogin, 
            BindingResult result, Model model, HttpSession session) {
        User user = userServ.login(newLogin, result);
        if(result.hasErrors()) {
            model.addAttribute("newUser", new User());
            return "index.jsp";
        }
        session.setAttribute("user_id", user.getId());
        return "redirect:/home";
    }
    
    @GetMapping("/classForm")
    public String classForm(Model model, HttpSession session) {
    	model.addAttribute("user", userServ.findUser((Long) session.getAttribute("user_id")));
    	model.addAttribute("newClass", new Class());
    	return "classForm.jsp";
    }
    
    
    
    @RequestMapping(value="/addClass", method=RequestMethod.POST)
    public String create(@Valid @ModelAttribute("newClass") Class classe, BindingResult result) {
        if(result.hasErrors()) {
            return "classForm.jsp";
        }
        else {
            classServ.createClass(classe);
            return "redirect:/home";
        }
    }
    
    @RequestMapping(value="/addStudent/{id}", method=RequestMethod.POST)
    public String createStudent(@Valid @ModelAttribute("newStudent") Student student,@PathVariable("id") Long id, BindingResult result) {
        if(result.hasErrors()) {
            return "singleClass.jsp";
        }
        else {
            studentServ.createStudent(student);
            return "redirect:/class/" + id;
        }
    }
    
    @GetMapping("/class/{id}")
    public String singleClass(@Valid @ModelAttribute("newStudent") Student newStudent, @PathVariable("id") Long id, Model model, HttpSession session) {
    	Class classe = classServ.findClass(id);
    	List<Student> classStudents = classe.getStudents();
    	List<Student> students = studentServ.allStudents();
    	students.removeIf(studentt -> (classStudents.contains(studentt)));
    	model.addAttribute("students", students);
    	model.addAttribute("classStudents", classStudents);
    	model.addAttribute("user", userServ.findUser((Long) session.getAttribute("user_id")));
    	model.addAttribute("classe", classServ.findClass(id));
    	return "singleClass.jsp";
    }
    
    @RequestMapping(value="/class/{id}/add", method=RequestMethod.POST)
	public String addStudentToClass(@RequestParam("student") Long studentId, @PathVariable("id") Long id) {
//		Student student = studentServ.findStudent(studentId);
//		student.addClass(classServ.findClass(id));
//		studentServ.updateStudent(student);
		Class classe = classServ.findClass(id);
		classe.addStudent(studentServ.findStudent(studentId));
		classServ.updateClass(classe);
		return "redirect:/class/" + id;
	}
    
//	@RequestMapping(value="/categories/{id}/add", method=RequestMethod.POST)
//	public String addProduct(@RequestParam("product") Long prodId, @PathVariable("id") Long id) {
//		Product product = prodService.findProduct(prodId);
//		product.addCategory(catService.findCategory(id));
//		prodService.updateProduct(product);
//		return "redirect:/categories/" + id;
//	}
    
    
//	@RequestMapping("/categories/{id}")
//	public String showCategory(@PathVariable("id") Long id, Model model) {
//		Category cat = catService.findCategory(id);
//		List<Product> catProds = cat.getProducts();
//		List<Product> prods = prodService.allProducts();
//		prods.removeIf(prod -> (catProds.contains(prod)));
//		model.addAttribute("category", cat);
//		model.addAttribute("products", prods);
//		model.addAttribute("catProds", catProds);
//		return "category.jsp";
//	}
    
    @RequestMapping("/class/edit/{id}")
    public String edit(@PathVariable("id") Long id, Model model, HttpSession session) {
        Class classe = classServ.findClass(id);
        model.addAttribute("classe", classe);
    	model.addAttribute("user", userServ.findUser((Long) session.getAttribute("user_id")));
        return "edit.jsp";
    }
    
    @PostMapping("/edit/{id}")
    public String edit(@Valid @ModelAttribute("classe") Class classe, BindingResult result, @PathVariable("id") Long id) {
        if (result.hasErrors()) {
            return "edit.jsp";
        } else {
            classServ.editClass(id, classe.getName(), classe.getWeekday(), classe.getPrice(), classe.getTime(), classe.getDescription());
            return "redirect:/home";
        }
    }
    
    @RequestMapping("/logout")
    public String logout(HttpSession session) {
    	session.removeAttribute("user_id");
    	return "redirect:/";
    }
    
    @PostMapping(value="/delete/{id}")
    public String destroy(@PathVariable("id") Long id) {
        classServ.deleteClass(id);
        return "redirect:/home";
    }
}