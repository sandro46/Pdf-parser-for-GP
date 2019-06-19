import sys, os
# sys.path.insert(0, 'lib')
# sys.path.append('../')

from lib.parser import *


class TestFibgen:
    def test_merge_pdf_files_create_merged_file_returns_none(self):
        testdir = '/home/beyond_eternity/PyQTDisigner/ParseGP/testpdfdir'
        merge_files(testdir)
        assert os.path.isfile(testdir+'/result.pdf')

    # def test_extract_text_returns_string(self):
    #     extract_text('/home/beyond_eternity/Загрузки/08.05.2019.pdf', './testdir')
    #     assert os.path.isfile('./testdir/11/13564.pdf')

    def test_parse_text_returns_usercode(self):
        text = """ООО "Бюро Финансовых споров"
                    Сч. N
                     40702810300280000154
                    Плательщик
                    АО "ОТП БАНК" г. Москва
                    Банк плательщика
                    ВОЛГО-ВЯТСКОЕ ГУ БАНКА РОССИИ г. Нижний
                    Новгород
                    БИК
                    Сч. N
                    044525311
                    30101810000000000311
                    БИК
                    Сч. N
                    042202001
                    Банк получателя
                    ИНН 5228003640
                     КПП 522801001
                    МЕЖРАЙОННАЯ ИФНС РОССИИ No 8 ПО
                    НИЖЕГОРОДСКОЙ ОБЛАСТИ
                    Сч. N
                     40101810400000010002
                    Вид оп.
                     01
                     Срок плат.
                    Наз. пл.
                     Очер. плат. 5
                    Получатель
                     Код
                     0
                     Рез. поле
                    18210803010011000110
                     22737000
                     0
                     0
                     0
                     0
                    госпошлина в суд от имени Алезер Менеджмент, Корп. за подачу заявления о выдаче судебного приказа к
                    Маринченко Дмитрий Викторович (внутр.код: 186/76932)
                    """
        result = parseText(text)
        assert len(result) > 0
        assert result[0] == '186'
        assert result[1] == '76932'