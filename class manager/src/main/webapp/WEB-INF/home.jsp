<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<%@ page isErrorPage="true" %>   
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="form" uri="http://www.springframework.org/tags/form" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@taglib prefix="fn" uri="http://java.sun.com/jsp/jstl/functions" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
	<h1>Welcome <c:out value="${user.userName}"/></h1>
	<a href="/logout">logout</a>
	<p>classes</p>
	<a href="/classForm">+ new class</a>
	
	<table>
		<tr>
			<td>Class Name</td>
			<td>Instructor</td>
			<td>Weekday</td>
			<td>Price</td>
			<td>Time</td>
		</tr>
		<c:forEach items="${classes}" var="classe">
			<tr>
				<td><a href="/class/${classe.id}"><c:out value="${classe.name}" /> </a>
					<c:if test="${user.id == classe.user.id}">
					<a href="/class/edit/${classe.id}">Edit</a>
				</c:if>
				</td>
				<td><c:out value="${classe.user.userName}" /></td>
				<td><c:out value="${classe.weekday}" /></td>
				<td>$<c:out value="${classe.price}" />.00</td>
				<c:set var="timeParts" value="${fn:split(classe.time, ':')}" />
				<fmt:parseNumber var = "i" type = "number" value = "${timeParts[0]}" />
				<c:choose>
					<c:when test="${timeParts[0] < 12}">
						<td><c:out value="${classe.time}" /> AM</td>
					</c:when>
					<c:otherwise>
						<td><c:out value="${timeParts[0] - 12}"/>:<c:out value="${timeParts[1]}"/> PM</td>
					</c:otherwise>
				</c:choose>

				
			</tr>
			</c:forEach>
	</table>
	
</body>
</html>