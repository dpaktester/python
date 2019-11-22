import Automate_Lupin_iPadRx_Report
import test_Lupin_ipad_Rx_report
from subprocess import call
import pytest

call(["pytest","C:\\Users\\dmahapatra\\PycharmProjects\\LupiniPadRx\\test_Lupin_ipad_Rx_report.py","pytest --html"])
#call(["pytest --html"])
#args_str = "-h C:\\Users\\dmahapatra\\PycharmProjects\\LupiniPadRx\\test_Lupin_ipad_Rx_report.py"
#pytest.cmdline.main(args_str.split(" "))