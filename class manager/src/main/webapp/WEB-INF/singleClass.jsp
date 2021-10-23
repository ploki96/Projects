<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page isErrorPage="true" %>   
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1><c:out value="${classe.name}"/> with <c:out value="${classe.user.userName}"/></h1>
	<p>Day: <c:out value="${classe.weekday}"/></p>
	<p>Cost: $<c:out value="${classe.price}"/></p>
	<p>Time: <c:out value="${classe.time}"/></p>
	<p><c:out value="${classe.description}"/></p>
	
			<h2>Students</h2>
			<ul>
				<c:forEach items="${classStudents}" var="student">
					<li><c:out value="${student.userName}" /> - <c:out value="${student.email}" /></li>
				</c:forEach>
			</ul>
			
	<div>
		<h1>Add Students to Class</h1>
		<p>New Student</p>
		<form:form action="/addStudent/${classe.id}" method="post" modelAttribute="newStudent">
        <div class="form-group">
            <label>Name: </label>
            <form:input path="userName" class="form-control" />
            <form:errors path="userName" class="text-danger" />
        </div>
        <div class="form-group">
            <label>Email: </label>
            <form:input path="email" class="form-control" />
            <form:errors path="email" class="text-danger" />
        </div>

        
        <input type="submit" value="Add Student" class="btn btn-primary" />
    </form:form>
		
		<form method="POST" action="/class/${classe.id}/add">
			<div>
				<label>Existing Student: </label>
				<select name="student">
				<c:forEach items="${students}" var="student">
					<option value="${student.id}"><c:out value="${student.userName}" /> - <c:out value="${student.email}" /></option>
				</c:forEach>
				</select>
			</div>
			<input type="submit" value="Add Student" />
		</form>
	</div>
			
</body>
</html>