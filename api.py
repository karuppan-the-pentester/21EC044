import requests

class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r

from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/api/', methods=['GET'])
def Api():


    Token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiZXhwIjoxNzE0NjM4OTM0LCJpYXQiOjE3MTQ2Mzg2MzQsImlzcyI6IkFmZm9yZG1lZCIsImp0aSI6ImQ1MzA5MmQ4LTEyN2MtNGRlYS04YTMyLThiZTIzNGExZjk4ZCIsInN1YiI6ImthcnVwcGFzYW15LjJrM0BnbWFpbC5jb20ifSwiY29tcGFueU5hbWUiOiJUZWNoTWFydCIsImNsaWVudElEIjoiZDUzMDkyZDgtMTI3Yy00ZGVhLThhMzItOGJlMjM0YTFmOThkIiwiY2xpZW50U2VjcmV0Ijoid3FhVG5jaElETkZUeHVYbiIsIm93bmVyTmFtZSI6IkthcnVwcGFzYW15Iiwib3duZXJFbWFpbCI6ImthcnVwcGFzYW15LjJrM0BnbWFpbC5jb20iLCJyb2xsTm8iOiIyMUVDMDQ0In0.Wn_z1g0d_I8ig3KZv3hsnW-2NTvocUR5GRFooNECLdA"
    FetchedProduct = requests.get(
        'http://20.244.56.144/test/companies/AMZ/categories/Laptop/products?top=100&minPrice=1&maxPrice=100000',
        auth=BearerAuth(Token))

    return FetchedProduct.json()

if __name__ == '__main__':
    app.run(debug=True)



