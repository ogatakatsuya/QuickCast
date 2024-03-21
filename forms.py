from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField
from wtforms.validators import ValidationError

class City(FlaskForm):
    city = SelectField('City:', choices=[('Hokkaido', '北海道'), ('Aomori', '青森県'), ('Iwate', '岩手県'), ('Miyagi', '宮城県'), ('Akita', '秋田県'),
                                    ('Yamagata', '山形県'), ('Fukushima', '福島県'), ('Ibaraki', '茨城県'), ('Tochigi', '栃木県'), ('Saitama', '埼玉県'),
                                    ('Chiba', '千葉県'), ('Tokyo', '東京都'), ('Kanagawa', '神奈川県'), ('Yamagata', '山形県'), ('Nagano', '長野県'),
                                    ('Niigata', '新潟県'), ('Toyama', '富山県'), ('Ishikawa', '石川県'), ('Fukui', '福井県'), ('Gifu', '岐阜県'),
                                    ('Shizuoka', '静岡県'), ('Aichi', '愛知県'), ('Mie', '三重県'), ('Shiga', '滋賀県'), ('Kyoto', '京都府'), ('Osaka', '大阪府'),
                                    ('Hyogo', '兵庫県'), ('Nara', '奈良県'), ('Wakayama', '和歌山県'), ('Tottori', '鳥取県'), ('Shimane', '島根県'),
                                    ('Okayama', '岡山県'), ('Hiroshima', '広島県'), ('Kochi', '高知県'), ('Fukuoka', '福岡県'), ('Saga', '佐賀県'),
                                    ('Nagasaki', '長崎県'), ('Kumamoto', '熊本県'), ('Oita', '大分県'), ('Miyazaki', '宮崎県'), ('Kagoshima', '鹿児島県'), ('Okinawa', '沖縄県')])
    submit = SubmitField('検索')