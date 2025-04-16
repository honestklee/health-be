from dataclasses import dataclass
from typing import Any
from flask import jsonify, make_response

@dataclass
class IReturnResponse:
    data: Any
    message: str
    statusCode: int

def success(values, message= "Success"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 200
    } 

    return make_response(jsonify(res)), 200

def invalid(values, message= "Invalid"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 202
    } 

    return make_response(jsonify(res)), 202

def badRequest(values, message= "Bad Request"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 400
    }

    return make_response(jsonify(res)), 400

def internalServerError(values, message= "Internal Server Error"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 500
    }

    return make_response(jsonify(res)), 500

def notFound(values, message = "Not Found"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 404
    }

    return make_response(jsonify(res)), 404

def unAuthorized(values, message= "Not Authorized"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 401
    }

    return make_response(jsonify(res)), 401

def forbidden(values, message = "Forbidden Access"):
    res = {
        'data' : values,
        'message' : message,
        'statusCode': 403
    }

    return make_response(jsonify(res)), 403
