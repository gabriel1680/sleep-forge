import pyActigraphy


class ActigraphyCalculator:

    def calculate(self, filepath: str) -> dict:
        raw_atr = pyActigraphy.io.read_raw_atr(input_fname=filepath)
        return {'DeviceID': raw_atr.uuid,
                'SubjectName': raw_atr.name,
                'IS': raw_atr.IS(binarize=False),
                'ISM': raw_atr.ISm(binarize=False),
                'ISp': raw_atr.ISp(binarize=False),
                'IV': raw_atr.IV(binarize=False),
                'IVm': raw_atr.IVm(binarize=False),
                'IVp': raw_atr.IVp(binarize=False),
                'L5': raw_atr.L5(binarize=False),
                'L5p': raw_atr.L5p(binarize=False),
                'M10': raw_atr.M10(binarize=False),
                'M10p': raw_atr.M10p(binarize=False),
                'PIM': raw_atr.PIM,
                'PIMn': raw_atr.PIMn,
                'RA': raw_atr.RA(binarize=False),
                'RAp': raw_atr.RAp(binarize=False),
                'SleepMidPoint': raw_atr.SleepMidPoint(),
                'SleepProfile': raw_atr.SleepProfile(),
                'SleepRegulatoryIndex': raw_atr.SleepRegularityIndex(),
                'SoD': raw_atr.SoD(binarize=False),
                'amb_light': raw_atr.amb_light,
                'average_daily_activity': raw_atr.average_daily_activity(),
                # 'average_daily_light': raw_atr.average_daily_light(),
                'blue_light': raw_atr.blue_light,
                'ir_light': raw_atr.ir_light,
                'light': raw_atr.light,
                'temperature': raw_atr.temperature,
                'white_light': raw_atr.white_light,
                'Roenneberg': raw_atr.Roenneberg(),
                'Roenneberg_AoT': raw_atr.Roenneberg_AoT(),
                # 'Crespo': raw_atr.Crespo(),
                #'Crespo_AoT': raw_atr.Crespo_AoT(),
                }
