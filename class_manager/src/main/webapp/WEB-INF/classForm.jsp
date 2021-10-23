<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page isErrorPage="true" %>    
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form"%> 
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1>Create a Course</h1>
	<a href="/home">back home</a>
	<form:form action="/addClass" method="post" modelAttribute="newClass">
        <div class="form-group">
            <label>Name: </label>
            <form:input path="name" class="form-control" />
            <form:errors path="name" class="text-danger" />
        </div>
        <div class="form-group">
            <label>Weekday: </label>
            <form:input path="weekday" class="form-control" />
            <form:errors path="weekday" class="text-danger" />
        </div>
        <div class="form-group">
            <label>Price: </label>
            <form:input type="number" path="price" class="form-control" />
            <form:errors path="price" class="text-danger" />
        </div>
        <div class="form-group">
            <label>Time: </label>
            <form:input type="time" path="time" class="form-control" />
            <form:errors path="time" class="text-danger" />
        </div>
        <div class="form-group">
            <label>Description: </label>
            <form:input path="description" class="form-control" />
            <form:errors path="description" class="text-danger" />
        </div>

            <form:hidden path="user" value="${user.id}" class="form-control" />


        
        <input type="submit" value="Add Course" class="btn btn-primary" />
    </form:form>
</body>
</html>