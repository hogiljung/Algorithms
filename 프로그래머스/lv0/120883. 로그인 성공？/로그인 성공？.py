def solution(id_pw, db):
    answer = 'fail'
    input_id, input_pw = id_pw
    for id, pw in db:
        if input_id == id:
            if input_pw == pw:
                answer = 'login'
            else:
                answer = 'wrong pw'
            return answer
    return answer