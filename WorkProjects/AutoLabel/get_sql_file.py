#!/usr/bin/env python3
# encoding: utf-8
'''
@author: Cai
@contact: yuwei.chen@yunzhenxin.com
@application:
@time: 2019/10/14 10:53
@desc: 将2kw数据按照既定配置文件进行标签化
'''

import pandas as pd

class Data2Tag(object):
    def __init__(self, config_df=None):
        if config_df is None:
            self.config_df = pd.read_csv(
                "/Users/cai/Desktop/pythonProjects/local_pyProjects/WorkProjects/AutoLabel/config_files/full_config.csv",
                sep='|', keep_default_na=False)
        else:
            self.config_df = config_df
        self.continuous_var = ['ft_app_ins_current_finance_cnt_avg'
            , 'ft_app_ins_current_finance_cnt_diff_m_llm'
            , 'ft_app_ins_current_finance_cnt_diff_m_lm'
            , 'ft_app_ins_current_finance_cnt_std'
            , 'ft_app_ins_current_micro_loan_cnt_avg'
            , 'ft_app_ins_current_micro_loan_cnt_diff_m_llm'
            , 'ft_app_ins_current_micro_loan_cnt_diff_m_lm'
            , 'ft_app_ins_current_micro_loan_cnt_std'
            , 'ft_app_ins_current_finance_cnt_m_rate'
            , 'ft_app_ins_current_debit_credit_cnt_m_rate'
            , 'ft_app_ins_current_micro_loan_cnt_m_rate'
            , 'ft_app_act_30d_finance_cnt_m_rate'
            , 'ft_app_act_30d_finance_times_m_rate'
            , 'ft_app_act_30d_finance_days_m_rate'
            , 'ft_app_act_30d_debit_credit_cnt_m_rate'
            , 'ft_app_act_30d_debit_credit_times_m_rate'
            , 'ft_app_act_30d_debit_credit_days_m_rate'
            , 'ft_app_act_30d_micro_loan_cnt_m_rate'
            , 'ft_app_act_30d_micro_loan_times_m_rate'
            , 'ft_app_act_30d_micro_loan_days_m_rate'
            , 'ft_app_ins_current_finance_cnt_cv'
            , 'ft_app_ins_current_debit_credit_cnt_cv'
            , 'ft_app_ins_current_micro_loan_cnt_cv'
            , 'ft_app_act_30d_finance_cnt_cv'
            , 'ft_app_act_30d_finance_times_cv'
            , 'ft_app_act_30d_finance_days_cv'
            , 'ft_app_act_30d_debit_credit_cnt_cv'
            , 'ft_app_act_30d_debit_credit_times_cv'
            , 'ft_app_act_30d_debit_credit_days_cv'
            , 'ft_app_act_30d_micro_loan_cnt_cv'
            , 'ft_app_act_30d_micro_loan_times_cv'
            , 'ft_app_act_30d_micro_loan_days_cv'
            , 'ft_app_ins_current_risk_cnt'
            , 'ft_app_ins_history_risk_cnt'
            , 'ft_app_ins_current_cheating_cnt'
            , 'ft_app_ins_history_cheating_cnt'
            , 'ft_app_ins_current_imei_alter_cnt'
            , 'ft_app_ins_history_imei_alter_cnt'
            , 'ft_app_ins_current_malicious_cnt'
            , 'ft_app_ins_history_malicious_cnt'
            , 'ft_dev_battery_use_30d_whole_nighttime_hours'
            , 'ft_dev_battery_use_30d_weekday_allday_hours'
            , 'ft_dev_battery_use_30d_weekday_worktime_hours'
            , 'ft_dev_battery_use_30d_weekday_closetime_hours'
            , 'ft_dev_battery_use_30d_weekday_nighttime_hours'
            , 'ft_dev_battery_use_30d_weekend_allday_hours'
            , 'ft_dev_battery_all_90d_whole_allday_hours'
            , 'ft_dev_battery_full_90d_whole_allday_hours'
            , 'ft_dev_battery_full_90d_weekday_allday_hours'
            , 'ft_dev_battery_full_90d_weekend_allday_hours'
            , 'ft_dev_battery_charge_90d_whole_allday_hours'
            , 'ft_dev_battery_charge_90d_weekday_allday_hours'
            , 'ft_dev_battery_charge_90d_weekend_allday_hours'
            , 'ft_dev_battery_use_90d_whole_allday_hours'
            , 'ft_dev_battery_use_90d_whole_worktime_hours'
            , 'ft_dev_battery_use_90d_whole_closetime_hours'
            , 'ft_dev_battery_use_90d_whole_nighttime_hours'
            , 'ft_dev_battery_use_90d_weekday_allday_hours'
            , 'ft_dev_battery_use_90d_weekday_worktime_hours'
            , 'ft_dev_battery_use_90d_weekday_closetime_hours'
            , 'ft_dev_battery_use_90d_weekday_nighttime_hours'
            , 'ft_dev_battery_use_90d_weekend_allday_hours'
            , 'ft_dev_ip_30d_whole_allday_cnt'
            , 'ft_dev_wifimac_30d_whole_allday_cnt'
            , 'ft_dev_wifimac_30d_whole_allday_days'
            , 'ft_dev_ip_30d_whole_worktime_cnt'
            , 'ft_dev_ip_30d_whole_closetime_cnt'
            , 'ft_dev_ip_30d_whole_nighttime_cnt'
            , 'ft_dev_ip_30d_weekday_allday_cnt'
            , 'ft_dev_ip_30d_weekday_worktime_cnt'
            , 'ft_dev_ip_30d_weekday_closetime_cnt'
            , 'ft_dev_ip_30d_weekday_nighttime_cnt'
            , 'ft_dev_ip_30d_weekend_allday_cnt'
            , 'ft_dev_wifimac_30d_whole_worktime_cnt'
            , 'ft_dev_wifimac_30d_whole_closetime_cnt'
            , 'ft_dev_wifimac_30d_whole_nighttime_cnt'
            , 'ft_dev_wifimac_30d_weekday_allday_cnt'
            , 'ft_dev_wifimac_30d_weekday_worktime_cnt'
            , 'ft_dev_wifimac_30d_weekday_closetime_cnt'
            , 'ft_dev_wifimac_30d_weekday_nighttime_cnt'
            , 'ft_dev_wifimac_30d_weekend_allday_cnt'
            , 'ft_dev_wifimac_30d_whole_worktime_days'
            , 'ft_dev_wifimac_30d_whole_closetime_days'
            , 'ft_dev_wifimac_30d_whole_nighttime_days'
            , 'ft_dev_wifimac_30d_weekday_allday_days'
            , 'ft_dev_wifimac_30d_weekday_worktime_days'
            , 'ft_dev_wifimac_30d_weekday_closetime_days'
            , 'ft_dev_wifimac_30d_weekday_nighttime_days'
            , 'ft_dev_wifimac_30d_weekend_allday_days'
            , 'ft_act_2week_rest_active_period_ls_hour0_4'
            , 'ft_act_2week_rest_active_period_ls_hour12_13'
            , 'ft_act_2week_rest_active_period_ls_hour13_18'
            , 'ft_act_2week_rest_active_period_ls_hour18_23'
            , 'ft_act_2week_rest_active_period_ls_hour5_7'
            , 'ft_act_2week_rest_active_period_ls_hour8_11'
            , 'ft_act_2week_work_active_period_ls_hour0_4'
            , 'ft_act_2week_work_active_period_ls_hour12_13'
            , 'ft_act_2week_work_active_period_ls_hour13_18'
            , 'ft_act_2week_work_active_period_ls_hour18_23'
            , 'ft_act_2week_work_active_period_ls_hour5_7'
            , 'ft_act_2week_work_active_period_ls_hour8_11'
            , 'ft_act_2week_rest_less_act_times'
            , 'ft_act_2week_rest_most_act_times'
            , 'ft_act_2week_rest_sum_act_times'
            , 'ft_act_2week_work_less_act_times'
            , 'ft_act_2week_work_most_act_times'
            , 'ft_act_2week_work_sum_act_times'
            , 'ft_app_act_30d_allcate_cnt'
            , 'ft_app_act_30d_allcate_times'
            , 'ft_app_act_30d_allcate_days'
            , 'ft_app_act_30d_fitness_cnt'
            , 'ft_app_act_30d_fitness_times'
            , 'ft_app_act_30d_fitness_days'
            , 'ft_app_act_30d_office_business_cnt'
            , 'ft_app_act_30d_office_business_times'
            , 'ft_app_act_30d_office_business_days'
            , 'ft_app_act_30d_video_cnt'
            , 'ft_app_act_30d_video_times'
            , 'ft_app_act_30d_video_days'
            , 'ft_app_act_30d_photo_cnt'
            , 'ft_app_act_30d_insurance_cnt'
            , 'ft_app_act_30d_insurance_times'
            , 'ft_app_act_30d_insurance_days'
            , 'ft_app_act_30d_credit_card_cnt'
            , 'ft_app_act_30d_credit_card_times'
            , 'ft_app_act_30d_credit_card_days'
            , 'ft_app_act_30d_debit_credit_cnt'
            , 'ft_app_act_30d_debit_credit_times'
            , 'ft_app_act_30d_debit_credit_days'
            , 'ft_app_act_30d_lottery_cnt'
            , 'ft_app_act_30d_lottery_times'
            , 'ft_app_act_30d_lottery_days'
            , 'ft_app_act_30d_invest_cnt'
            , 'ft_app_act_30d_invest_times'
            , 'ft_app_act_30d_invest_days'
            , 'ft_app_act_30d_payment_cnt'
            , 'ft_app_act_30d_payment_times'
            , 'ft_app_act_30d_payment_days'
            , 'ft_app_act_30d_money_management_cnt'
            , 'ft_app_act_30d_money_management_times'
            , 'ft_app_act_30d_money_management_days'
            , 'ft_app_act_30d_tally_cnt'
            , 'ft_app_act_30d_tally_times'
            , 'ft_app_act_30d_tally_days'
            , 'ft_app_act_30d_bank_cnt'
            , 'ft_app_act_30d_bank_times'
            , 'ft_app_act_30d_bank_days'
            , 'ft_app_act_30d_online_gamble_cnt'
            , 'ft_app_act_30d_online_gamble_times'
            , 'ft_app_act_30d_online_gamble_days'
            , 'ft_app_act_30d_micro_loan_cnt'
            , 'ft_app_act_30d_micro_loan_times'
            , 'ft_app_act_30d_micro_loan_days'
            , 'ft_app_act_30d_finance_cnt'
            , 'ft_app_act_30d_finance_times'
            , 'ft_app_act_30d_finance_days'
            , 'ft_finance_score_c'
            , 'ft_finance_score_d'
            , 'ft_finance_score_e'
            , 'ft_finance_score_f'
            , 'ft_app_ins_current_gpscheat_cnt'
            , 'ft_app_ins_history_gpscheat_cnt'
            , 'ft_app_ins_current_simulator_cnt'
            , 'ft_app_ins_history_simulator_cnt'
            , 'ft_app_act_30d_risk_cnt'
            , 'ft_app_act_30d_risk_times'
            , 'ft_app_act_30d_risk_days'
            , 'ft_app_act_30d_cheating_cnt'
            , 'ft_app_act_30d_cheating_times'
            , 'ft_app_act_30d_cheating_days'
            , 'ft_app_act_30d_imei_alter_cnt'
            , 'ft_app_act_30d_imei_alter_times'
            , 'ft_app_act_30d_imei_alter_days'
            , 'ft_app_act_30d_malicious_cnt'
            , 'ft_app_act_30d_malicious_times'
            , 'ft_app_act_30d_malicious_days'
            , 'ft_app_act_30d_gpscheat_cnt'
            , 'ft_app_act_30d_gpscheat_times'
            , 'ft_app_act_30d_gpscheat_days'
            , 'ft_app_act_30d_simulator_cnt'
            , 'ft_app_act_30d_simulator_times'
            , 'ft_app_act_30d_simulator_days'
            , 'ft_dev_storage'
            , 'ft_dev_free_storage'
            , 'ft_dev_storage_usage_ratio'
            , 'ft_gezhen_multi_loan_score'
            , 'ft_safe_score_c'
            , 'ft_safe_score_d'
            , 'ft_safe_score_e'
            , 'ft_safe_score_f'
            , 'ft_dev_battery_full_30d_whole_allday_hours'
            , 'ft_dev_battery_charge_30d_whole_allday_hours'
            , 'ft_dev_battery_use_30d_whole_allday_hours'
            , 'ft_dev_battery_all_30d_whole_allday_hours'
            , 'ft_dev_battery_full_30d_weekday_allday_hours'
            , 'ft_dev_battery_full_30d_weekend_allday_hours'
            , 'ft_dev_battery_charge_30d_weekday_allday_hours'
            , 'ft_dev_battery_charge_30d_weekend_allday_hours'
            , 'ft_dev_battery_use_30d_whole_worktime_hours'
            , 'ft_dev_battery_use_30d_whole_closetime_hours'
            , 'ft_app_ins_current_money_management_cnt'
            , 'ft_app_ins_history_money_management_cnt'
            , 'ft_app_ins_current_tally_cnt'
            , 'ft_app_ins_history_tally_cnt'
            , 'ft_app_ins_current_bank_cnt'
            , 'ft_app_ins_history_bank_cnt'
            , 'ft_app_ins_current_online_gamble_cnt'
            , 'ft_app_ins_history_online_gamble_cnt'
            , 'ft_app_ins_current_micro_loan_cnt'
            , 'ft_app_ins_history_micro_loan_cnt'
            , 'ft_app_ins_history_shortterm_loan'
            , 'ft_app_ins_current_shortterm_loan'
            , 'ft_app_act_30d_gamble_cnt'
            , 'ft_app_act_30d_gamble_times'
            , 'ft_app_act_30d_gamble_days'
            , 'ft_act_month_rest_active_period_ls_hour0_4'
            , 'ft_act_month_rest_active_period_ls_hour12_13'
            , 'ft_act_month_rest_active_period_ls_hour13_18'
            , 'ft_act_month_rest_active_period_ls_hour18_23'
            , 'ft_act_month_rest_active_period_ls_hour5_7'
            , 'ft_act_month_rest_active_period_ls_hour8_11'
            , 'ft_act_month_rest_less_act_times'
            , 'ft_act_month_rest_most_act_times'
            , 'ft_act_month_rest_sum_act_times'
            , 'ft_act_month_work_active_period_ls_hour0_4'
            , 'ft_act_month_work_active_period_ls_hour8_11'
            , 'ft_act_month_work_active_period_ls_hour12_13'
            , 'ft_act_month_work_active_period_ls_hour13_18'
            , 'ft_act_month_work_active_period_ls_hour18_23'
            , 'ft_act_month_work_active_period_ls_hour5_7'
            , 'ft_act_month_work_less_act_times'
            , 'ft_act_month_work_most_act_times'
            , 'ft_act_month_work_sum_act_times'
            , 'ft_app_ins_current_fitness_cnt'
            , 'ft_app_ins_history_fitness_cnt'
            , 'ft_app_ins_current_photo_cnt'
            , 'ft_app_ins_history_photo_cnt'
            , 'ft_app_ins_current_life_casual_cnt'
            , 'ft_app_ins_history_life_casual_cnt'
            , 'ft_app_ins_current_office_business_cnt'
            , 'ft_app_ins_history_office_business_cnt'
            , 'ft_app_ins_current_video_cnt'
            , 'ft_app_ins_history_video_cnt'
            , 'ft_app_ins_current_news_reading_cnt'
            , 'ft_app_ins_history_news_reading_cnt'
            , 'ft_app_ins_current_game_cnt'
            , 'ft_app_ins_history_game_cnt'
            , 'ft_app_ins_current_examination_cnt'
            , 'ft_app_ins_history_examination_cnt'
            , 'ft_app_ins_current_child_rearing_cnt'
            , 'ft_app_ins_history_child_rearin_cnt'
            , 'ft_app_ins_current_messaging_social_cnt'
            , 'ft_app_ins_history_messaging_social_cnt'
            , 'ft_app_ins_current_short_video_cnt'
            , 'ft_app_ins_history_short_video_cnt'
            , 'ft_app_ins_current_live_cnt'
            , 'ft_app_ins_history_live_cnt'
            , 'ft_act_cate_num'
            , 'ft_act_max_act_time'
            , 'ft_act_pkg_num'
            , 'ft_ins_cate_app_cnt_ls_100000'
            , 'ft_ins_cate_app_cnt_ls_120000'
            , 'ft_ins_cate_app_cnt_ls_130000'
            , 'ft_ins_cate_app_cnt_ls_140000'
            , 'ft_ins_cate_app_cnt_ls_150000'
            , 'ft_ins_cate_app_cnt_ls_160000'
            , 'ft_ins_cate_app_cnt_ls_170000'
            , 'ft_ins_cate_app_cnt_ls_190000'
            , 'ft_ins_cate_app_cnt_ls_200000'
            , 'ft_ins_cate_app_cnt_ls_210000'
            , 'ft_ins_cate_app_cnt_ls_220000'
            , 'ft_ins_cate_app_cnt_ls_230000'
            , 'ft_ins_cate_app_cnt_ls_240000'
            , 'ft_ins_cate_app_cnt_ls_250000'
            , 'ft_ins_cate_app_cnt_ls_270000'
            , 'ft_ins_cate_app_cnt_ls_290000'
            , 'ft_ins_cate_app_cnt_ls_300000'
            , 'ft_ins_cate_app_cnt_ls_900400'
            , 'ft_ins_cate_app_cnt_ls_900500'
            , 'ft_ins_cate_app_cnt_ls_900600'
            , 'ft_ins_cate_app_cnt_ls_900700'
            , 'ft_ins_category_cnt'
            , 'ft_ins_largest_cate_cnt'
            , 'ft_ins_pkg_cnt'
            , 'ft_lbs_city_stay_oneday_cnt'
            , 'ft_lbs_city_stay_twoday_cnt'
            , 'ft_stable_score_a'
            , 'ft_stable_score_c'
            , 'ft_stable_score_e'
            , 'ft_app_act_30d_debit_credit_cnt_avg'
            , 'ft_app_act_30d_debit_credit_cnt_diff_m_llm'
            , 'ft_app_act_30d_debit_credit_cnt_diff_m_lm'
            , 'ft_app_act_30d_debit_credit_cnt_std'
            , 'ft_app_act_30d_debit_credit_days_avg'
            , 'ft_app_act_30d_debit_credit_days_diff_m_llm'
            , 'ft_app_act_30d_debit_credit_days_diff_m_lm'
            , 'ft_app_act_30d_debit_credit_days_std'
            , 'ft_app_act_30d_debit_credit_times_avg'
            , 'ft_app_act_30d_debit_credit_times_diff_m_llm'
            , 'ft_app_act_30d_debit_credit_times_diff_m_lm'
            , 'ft_app_act_30d_debit_credit_times_std'
            , 'ft_app_act_30d_finance_cnt_avg'
            , 'ft_app_act_30d_finance_cnt_diff_m_llm'
            , 'ft_app_act_30d_finance_cnt_diff_m_lm'
            , 'ft_app_act_30d_finance_cnt_std'
            , 'ft_app_act_30d_finance_days_avg'
            , 'ft_app_act_30d_finance_days_diff_m_llm'
            , 'ft_app_act_30d_finance_days_diff_m_lm'
            , 'ft_app_act_30d_finance_days_std'
            , 'ft_app_act_30d_finance_times_avg'
            , 'ft_app_act_30d_finance_times_diff_m_llm'
            , 'ft_app_act_30d_finance_times_diff_m_lm'
            , 'ft_app_act_30d_finance_times_std'
            , 'ft_app_act_30d_micro_loan_cnt_avg'
            , 'ft_app_act_30d_micro_loan_cnt_diff_m_llm'
            , 'ft_app_act_30d_micro_loan_cnt_diff_m_lm'
            , 'ft_app_act_30d_micro_loan_cnt_std'
            , 'ft_app_act_30d_micro_loan_days_avg'
            , 'ft_app_act_30d_micro_loan_days_diff_m_llm'
            , 'ft_app_act_30d_micro_loan_days_diff_m_lm'
            , 'ft_app_act_30d_micro_loan_days_std'
            , 'ft_app_act_30d_micro_loan_times_avg'
            , 'ft_app_act_30d_micro_loan_times_diff_m_llm'
            , 'ft_app_act_30d_micro_loan_times_diff_m_lm'
            , 'ft_app_act_30d_micro_loan_times_std'
            , 'ft_app_ins_current_debit_credit_cnt_avg'
            , 'ft_app_ins_current_debit_credit_cnt_diff_m_llm'
            , 'ft_app_ins_current_debit_credit_cnt_diff_m_lm'
            , 'ft_app_ins_current_debit_credit_cnt_std'
            , 'ft_app_act_30d_market_days'
            , 'ft_app_ins_current_online_shopping_cnt'
            , 'ft_app_ins_history_online_shopping_cnt'
            , 'ft_app_ins_current_travel_cnt'
            , 'ft_app_ins_history_travel_cnt'
            , 'ft_app_ins_current_discounts_cnt'
            , 'ft_app_ins_history_discounts_cnt'
            , 'ft_app_ins_current_market_cnt'
            , 'ft_app_ins_history_market_cnt'
            , 'ft_lbs_home_cons_ls_high'
            , 'ft_lbs_home_cons_ls_low'
            , 'ft_lbs_home_cons_ls_middle'
            , 'ft_lbs_pwoi_all_mostoften_consume_high'
            , 'ft_lbs_pwoi_all_mostoften_consume_low'
            , 'ft_lbs_pwoi_all_mostoften_consume_middle'
            , 'ft_lbs_pwoi_all_often_consum_high'
            , 'ft_lbs_pwoi_all_often_consum_low'
            , 'ft_lbs_pwoi_all_often_consum_middle'
            , 'ft_lbs_work_cons_ls_high'
            , 'ft_lbs_work_cons_ls_low'
            , 'ft_lbs_work_cons_ls_middle'
            , 'ft_consumption_score_a'
            , 'ft_consumption_score_c'
            , 'ft_consumption_score_e'
            , 'ft_app_ins_current_finance_cnt'
            , 'ft_app_ins_history_finance_cnt'
            , 'ft_app_ins_current_gamble_cnt'
            , 'ft_app_ins_history_gamble_cnt'
            , 'ft_app_ins_current_insurance_cnt'
            , 'ft_app_ins_history_insurance_cnt'
            , 'ft_app_ins_current_credit_card_cnt'
            , 'ft_app_ins_history_credit_card_cnt'
            , 'ft_app_ins_current_debit_credit_cnt'
            , 'ft_app_ins_history_debit_credit_cnt'
            , 'ft_app_ins_current_lottery_cnt'
            , 'ft_app_ins_history_lottery_cnt'
            , 'ft_app_ins_current_invest_cnt'
            , 'ft_app_ins_history_invest_cnt'
            , 'ft_app_ins_current_payment_cnt'
            , 'ft_app_ins_history_payment_cnt'
            , 'ft_app_act_30d_photo_times'
            , 'ft_app_act_30d_photo_days'
            , 'ft_app_act_30d_news_reading_cnt'
            , 'ft_app_act_30d_news_reading_times'
            , 'ft_app_act_30d_news_reading_days'
            , 'ft_app_act_30d_game_cnt'
            , 'ft_app_act_30d_game_times'
            , 'ft_app_act_30d_game_days'
            , 'ft_app_act_30d_life_casual_cnt'
            , 'ft_app_act_30d_life_casual_times'
            , 'ft_app_act_30d_life_casual_days'
            , 'ft_app_act_30d_examination_cnt'
            , 'ft_app_act_30d_examination_times'
            , 'ft_app_act_30d_examination_days'
            , 'ft_app_act_30d_child_rearin_cnt'
            , 'ft_app_act_30d_child_rearin_times'
            , 'ft_app_act_30d_child_rearin_days'
            , 'ft_app_act_30d_messaging_social_cnt'
            , 'ft_app_act_30d_messaging_social_times'
            , 'ft_app_act_30d_messaging_social_days'
            , 'ft_app_act_30d_short_video_cnt'
            , 'ft_app_act_30d_short_video_times'
            , 'ft_app_act_30d_short_video_days'
            , 'ft_app_act_30d_live_cnt'
            , 'ft_app_act_30d_live_times'
            , 'ft_app_act_30d_live_days'
            , 'ft_asset_score_a'
            , 'ft_asset_score_c'
            , 'ft_asset_score_e'
            , 'ft_app_act_30d_online_shopping_cnt'
            , 'ft_app_act_30d_online_shopping_times'
            , 'ft_app_act_30d_online_shopping_days'
            , 'ft_app_act_30d_travel_cnt'
            , 'ft_app_act_30d_travel_times'
            , 'ft_app_act_30d_travel_days'
            , 'ft_app_act_30d_discounts_cnt'
            , 'ft_app_act_30d_discounts_times'
            , 'ft_app_act_30d_discounts_days'
            , 'ft_app_act_30d_market_cnt'
            , 'ft_app_act_30d_market_times']
        self.blacklist_var = ["ft_gz_black_list", "ft_gz_grey_list"]
        self.class_var = ['ft_act_2week_rest_less_act_period_ls_hour12_13'
            , 'ft_act_2week_rest_less_act_period_ls_hour5_7'
            , 'ft_cross_lbs_4wr_act_cnt_app_4w_unins'
            , 'ft_cross_lbs_staycity_tag_021700'
            , 'ft_cross_most_act_cate_lbs_staycity'
            , 'ft_cross_tag_travel_macao_cnt'
            , 'ft_dev_all_nighter'
            , 'ft_dev_deprecia_price'
            , 'ft_dev_gid2imei_2w_cnt'
            , 'ft_dev_gid2imsi_2w_cnt'
            , 'ft_dev_gid2mac_2w_cnt'
            , 'ft_dev_market_price'
            , 'ft_dev_market_year'
            , 'ft_dev_root'
            , 'ft_dev_root_blacklist'
            , 'ft_dev_trust'
            , 'ft_dev_virtual'
            , 'ft_dev_xposed'
            , 'ft_gezhen_multi_loan_level'
            , 'ft_gz_sensitive_area'
            , 'ft_lbs_entertainment_a_12w_days'
            , 'ft_lbs_entertainment_b_12w_days'
            , 'ft_lbs_entertainment_c_12w_days'
            , 'ft_lbs_entertainment_d_12w_days'
            , 'ft_lbs_entertainment_e_12w_days'
            , 'ft_lbs_entertainment_f_12w_days'
            , 'ft_lbs_hospital_12w_days'
            , 'ft_social_blackfriends'
            , 'ft_social_blackfriends_group'
            , 'ft_tag_banking'
            , 'ft_tag_bas_fraudster'
            , 'ft_tag_bookkeeping'
            , 'ft_tag_credit_card'
            , 'ft_tag_fitness'
            , 'ft_tag_health'
            , 'ft_tag_language_learing'
            , 'ft_tag_lottery'
            , 'ft_tag_online_learing'
            , 'ft_act_2week_rest_most_act_period_ls_hour13_18'
            , 'ft_act_2week_rest_most_act_period_ls_hour18_23'
            , 'ft_act_2week_rest_most_act_period_ls_hour8_11'
            , 'ft_act_2week_work_most_act_period_ls_hour13_18'
            , 'ft_act_2week_work_most_act_period_ls_hour18_23'
            , 'ft_act_2week_work_most_act_period_ls_hour8_11'
            , 'ft_act_cate_ls_100000'
            , 'ft_act_cate_ls_120000'
            , 'ft_act_cate_ls_140000'
            , 'ft_act_cate_ls_150000'
            , 'ft_act_cate_ls_160000'
            , 'ft_act_cate_ls_200000'
            , 'ft_act_cate_ls_210000'
            , 'ft_act_cate_ls_220000'
            , 'ft_act_cate_ls_230000'
            , 'ft_act_cate_ls_240000'
            , 'ft_act_cate_ls_270000'
            , 'ft_act_cate_ls_300000'
            , 'ft_act_month_rest_less_act_period_ls_hour0_4'
            , 'ft_act_month_rest_less_act_period_ls_hour12_13'
            , 'ft_act_month_rest_less_act_period_ls_hour5_7'
            , 'ft_act_month_rest_most_act_period_ls_hour13_18'
            , 'ft_act_month_rest_most_act_period_ls_hour18_23'
            , 'ft_act_month_rest_most_act_period_ls_hour8_11'
            , 'ft_act_month_work_less_act_period_ls_hour0_4'
            , 'ft_act_month_work_less_act_period_ls_hour12_13'
            , 'ft_act_month_work_less_act_period_ls_hour5_7'
            , 'ft_act_month_work_less_act_period_ls_hour8_11'
            , 'ft_act_month_work_most_act_period_ls_hour13_18'
            , 'ft_act_month_work_most_act_period_ls_hour18_23'
            , 'ft_act_month_work_most_act_period_ls_hour8_11'
            , 'ft_andr_t1_most_interest_ls_021000'
            , 'ft_app_install_category_160000'
            , 'ft_app_uninstall_category_160000'
            , 'ft_asset_score_b'
            , 'ft_asset_score_d'
            , 'ft_asset_score_f'
            , 'ft_consumption_score_b'
            , 'ft_consumption_score_d'
            , 'ft_consumption_score_f'
            , 'ft_cross_act_160000_tag_0844'
            , 'ft_cross_blackfriends_act_2w_cat_16000'
            , 'ft_cross_blackfriends_tag_p2p'
            , 'ft_cross_ins_credit_ins_largest_cate_cnt'
            , 'ft_cross_ins_loan_tag_business_travel'
            , 'ft_cross_ins_loan_tag_p2p'
            , 'ft_cross_ins_wifilocating_tag_credit_card'
            , 'ft_cross_lbs_staycity_ins_160000'
            , 'ft_cross_tag_city_level1_housing_price'
            , 'ft_cross_tag_city_level1_price'
            , 'ft_cross_tag_city_level2_housing_price'
            , 'ft_cross_tag_city_level2_price'
            , 'ft_cross_tag_city_level3_housing_price'
            , 'ft_cross_tag_city_level3_price'
            , 'ft_cross_tag_city_level4_housing_price'
            , 'ft_cross_tag_city_level4_price'
            , 'ft_cross_tag_college_student_tag_p2p'
            , 'ft_cross_tag_p2p_tag_lifeservice'
            , 'ft_cross_unins_app_ins_160000'
            , 'ft_dev_timezone'
            , 'ft_gz_car_price'
            , 'ft_gz_consumption_capacity'
            , 'ft_gz_housing_price_homeaddr_cnt'
            , 'ft_gz_income_1'
            , 'ft_ins_app_install_category_160000'
            , 'ft_ins_app_uninstall_category_120000'
            , 'ft_ins_app_uninstall_category_140000'
            , 'ft_ins_app_uninstall_category_150000'
            , 'ft_ins_app_uninstall_category_160000'
            , 'ft_ins_app_uninstall_category_190000'
            , 'ft_ins_app_uninstall_category_200000'
            , 'ft_ins_app_uninstall_category_210000'
            , 'ft_ins_app_uninstall_category_230000'
            , 'ft_ins_app_uninstall_category_240000'
            , 'ft_ins_app_uninstall_category_270000'
            , 'ft_ins_app_uninstall_category_300000'
            , 'ft_ins_app_uninstall_category_900400'
            , 'ft_ins_largest_cate_ls_120000'
            , 'ft_ins_largest_cate_ls_140000'
            , 'ft_ins_largest_cate_ls_150000'
            , 'ft_ins_largest_cate_ls_190000'
            , 'ft_ins_largest_cate_ls_200000'
            , 'ft_ins_largest_cate_ls_210000'
            , 'ft_ins_largest_cate_ls_270000'
            , 'ft_lbs_airport_4w_times'
            , 'ft_lbs_dis_label'
            , 'ft_lbs_family_12w_change_cnt'
            , 'ft_lbs_family_12w_cnt'
            , 'ft_lbs_geo7_unusual'
            , 'ft_lbs_hotel_4w_days'
            , 'ft_lbs_hotel_4w_level'
            , 'ft_lbs_house_price'
            , 'ft_lbs_property_fee'
            , 'ft_lbs_residence_stability'
            , 'ft_lbs_same_night_stay_wifimac_cnt'
            , 'ft_lbs_stable_stops'
            , 'ft_lbs_trainstation_4w_times'
            , 'ft_lbs_work_12w_change_cnt'
            , 'ft_lbs_work_12w_cnt'
            , 'ft_lbs_workplace_stability'
            , 'ft_most_act_cate_ls_160000'
            , 'ft_stable_imsi_active_days'
            , 'ft_stable_imsi_changes'
            , 'ft_stable_imsi_used_days'
            , 'ft_stable_score_b'
            , 'ft_stable_score_d'
            , 'ft_stable_score_f'
            , 'ft_tag_age'
            , 'ft_tag_asset_management'
            , 'ft_tag_bourgeois'
            , 'ft_tag_car_ownership'
            , 'ft_tag_city_tier'
            , 'ft_tag_consumption_level'
            , 'ft_tag_consumption_range'
            , 'ft_tag_education'
            , 'ft_tag_gender'
            , 'ft_tag_hotel'
            , 'ft_tag_industry_ad'
            , 'ft_tag_industry_financial'
            , 'ft_tag_industry_it'
            , 'ft_tag_marrige'
            , 'ft_tag_occupation_entrepreneur'
            , 'ft_tag_occupation_it'
            , 'ft_tag_occupation_medical'
            , 'ft_tag_occupation_office'
            , 'ft_tag_occupation_teacher'
            , 'ft_tag_p2p'
            , 'ft_tag_parent_0to2y'
            , 'ft_tag_parent_3to6y'
            , 'ft_tag_parent_k1tok6'
            , 'ft_tag_parent_k7tok12'
            , 'ft_tag_primary_purchaser'
            , 'ft_tag_property_owner'
            , 'ft_tag_purchaser'
            , 'ft_tag_residence'
            , 'ft_tag_shopping'
            , 'ft_tag_stock'
            , 'ft_tag_travel'
            , 'mother'
            , 'parent'
            , 'ft_dev_phone_brand'
            , 'ft_dev_phone_model'
            , 'ft_app_act_30d_debit_credit_cnt_change'
            , 'ft_app_act_30d_debit_credit_days_change'
            , 'ft_app_act_30d_debit_credit_times_change'
            , 'ft_app_act_30d_finance_cnt_change'
            , 'ft_app_act_30d_finance_days_change'
            , 'ft_app_act_30d_finance_times_change'
            , 'ft_app_act_30d_micro_loan_cnt_change'
            , 'ft_app_act_30d_micro_loan_days_change'
            , 'ft_app_act_30d_micro_loan_times_change'
            , 'ft_app_ins_current_debit_credit_cnt_change'
            , 'ft_app_ins_current_finance_cnt_change'
            , 'ft_app_ins_current_micro_loan_cnt_change'
            , 'ft_tag_city'
            , 'ft_tag_province']
        self.all_columns = ['ft_app_act_30d_allcate_cnt',
                            'ft_app_act_30d_allcate_days',
                            'ft_app_act_30d_allcate_times',
                            'ft_app_act_30d_bank_cnt',
                            'ft_app_act_30d_bank_days',
                            'ft_app_act_30d_bank_times',
                            'ft_app_act_30d_cheating_cnt',
                            'ft_app_act_30d_cheating_days',
                            'ft_app_act_30d_cheating_times',
                            'ft_app_act_30d_child_rearin_cnt',
                            'ft_app_act_30d_child_rearin_days',
                            'ft_app_act_30d_child_rearin_times',
                            'ft_app_act_30d_credit_card_cnt',
                            'ft_app_act_30d_credit_card_days',
                            'ft_app_act_30d_credit_card_times',
                            'ft_app_act_30d_debit_credit_cnt',
                            'ft_app_act_30d_debit_credit_days',
                            'ft_app_act_30d_debit_credit_times',
                            'ft_app_act_30d_discounts_cnt',
                            'ft_app_act_30d_discounts_days',
                            'ft_app_act_30d_discounts_times',
                            'ft_app_act_30d_examination_cnt',
                            'ft_app_act_30d_examination_days',
                            'ft_app_act_30d_examination_times',
                            'ft_app_act_30d_finance_cnt',
                            'ft_app_act_30d_finance_days',
                            'ft_app_act_30d_finance_times',
                            'ft_app_act_30d_fitness_cnt',
                            'ft_app_act_30d_fitness_days',
                            'ft_app_act_30d_fitness_times',
                            'ft_app_act_30d_gamble_cnt',
                            'ft_app_act_30d_gamble_days',
                            'ft_app_act_30d_gamble_times',
                            'ft_app_act_30d_game_cnt',
                            'ft_app_act_30d_game_days',
                            'ft_app_act_30d_game_times',
                            'ft_app_act_30d_gpscheat_cnt',
                            'ft_app_act_30d_gpscheat_days',
                            'ft_app_act_30d_gpscheat_times',
                            'ft_app_act_30d_imei_alter_cnt',
                            'ft_app_act_30d_imei_alter_days',
                            'ft_app_act_30d_imei_alter_times',
                            'ft_app_act_30d_insurance_cnt',
                            'ft_app_act_30d_insurance_days',
                            'ft_app_act_30d_insurance_times',
                            'ft_app_act_30d_invest_cnt',
                            'ft_app_act_30d_invest_days',
                            'ft_app_act_30d_invest_times',
                            'ft_app_act_30d_life_casual_cnt',
                            'ft_app_act_30d_life_casual_days',
                            'ft_app_act_30d_life_casual_times',
                            'ft_app_act_30d_live_cnt',
                            'ft_app_act_30d_live_days',
                            'ft_app_act_30d_live_times',
                            'ft_app_act_30d_lottery_cnt',
                            'ft_app_act_30d_lottery_days',
                            'ft_app_act_30d_lottery_times',
                            'ft_app_act_30d_malicious_cnt',
                            'ft_app_act_30d_malicious_days',
                            'ft_app_act_30d_malicious_times',
                            'ft_app_act_30d_market_cnt',
                            'ft_app_act_30d_market_days',
                            'ft_app_act_30d_market_times',
                            'ft_app_act_30d_messaging_social_cnt',
                            'ft_app_act_30d_messaging_social_days',
                            'ft_app_act_30d_messaging_social_times',
                            'ft_app_act_30d_micro_loan_cnt',
                            'ft_app_act_30d_micro_loan_days',
                            'ft_app_act_30d_micro_loan_times',
                            'ft_app_act_30d_money_management_cnt',
                            'ft_app_act_30d_money_management_days',
                            'ft_app_act_30d_money_management_times',
                            'ft_app_act_30d_news_reading_cnt',
                            'ft_app_act_30d_news_reading_days',
                            'ft_app_act_30d_news_reading_times',
                            'ft_app_act_30d_office_business_cnt',
                            'ft_app_act_30d_office_business_days',
                            'ft_app_act_30d_office_business_times',
                            'ft_app_act_30d_online_gamble_cnt',
                            'ft_app_act_30d_online_gamble_days',
                            'ft_app_act_30d_online_gamble_times',
                            'ft_app_act_30d_online_shopping_cnt',
                            'ft_app_act_30d_online_shopping_days',
                            'ft_app_act_30d_online_shopping_times',
                            'ft_app_act_30d_payment_cnt',
                            'ft_app_act_30d_payment_days',
                            'ft_app_act_30d_payment_times',
                            'ft_app_act_30d_photo_cnt',
                            'ft_app_act_30d_photo_days',
                            'ft_app_act_30d_photo_times',
                            'ft_app_act_30d_risk_cnt',
                            'ft_app_act_30d_risk_days',
                            'ft_app_act_30d_risk_times',
                            'ft_app_act_30d_short_video_cnt',
                            'ft_app_act_30d_short_video_days',
                            'ft_app_act_30d_short_video_times',
                            'ft_app_act_30d_simulator_cnt',
                            'ft_app_act_30d_simulator_days',
                            'ft_app_act_30d_simulator_times',
                            'ft_app_act_30d_tally_cnt',
                            'ft_app_act_30d_tally_days',
                            'ft_app_act_30d_tally_times',
                            'ft_app_act_30d_travel_cnt',
                            'ft_app_act_30d_travel_days',
                            'ft_app_act_30d_travel_times',
                            'ft_app_act_30d_video_cnt',
                            'ft_app_act_30d_video_days',
                            'ft_app_act_30d_video_times',
                            'ft_app_ins_current_bank_cnt',
                            'ft_app_ins_current_cheating_cnt',
                            'ft_app_ins_current_child_rearing_cnt',
                            'ft_app_ins_current_credit_card_cnt',
                            'ft_app_ins_current_debit_credit_cnt',
                            'ft_app_ins_current_discounts_cnt',
                            'ft_app_ins_current_examination_cnt',
                            'ft_app_ins_current_finance_cnt',
                            'ft_app_ins_current_fitness_cnt',
                            'ft_app_ins_current_gamble_cnt',
                            'ft_app_ins_current_game_cnt',
                            'ft_app_ins_current_gpscheat_cnt',
                            'ft_app_ins_current_imei_alter_cnt',
                            'ft_app_ins_current_insurance_cnt',
                            'ft_app_ins_current_invest_cnt',
                            'ft_app_ins_current_life_casual_cnt',
                            'ft_app_ins_current_live_cnt',
                            'ft_app_ins_current_lottery_cnt',
                            'ft_app_ins_current_malicious_cnt',
                            'ft_app_ins_current_market_cnt',
                            'ft_app_ins_current_messaging_social_cnt',
                            'ft_app_ins_current_micro_loan_cnt',
                            'ft_app_ins_current_money_management_cnt',
                            'ft_app_ins_current_news_reading_cnt',
                            'ft_app_ins_current_office_business_cnt',
                            'ft_app_ins_current_online_gamble_cnt',
                            'ft_app_ins_current_online_shopping_cnt',
                            'ft_app_ins_current_payment_cnt',
                            'ft_app_ins_current_photo_cnt',
                            'ft_app_ins_current_risk_cnt',
                            'ft_app_ins_current_short_video_cnt',
                            'ft_app_ins_current_simulator_cnt',
                            'ft_app_ins_current_tally_cnt',
                            'ft_app_ins_current_travel_cnt',
                            'ft_app_ins_current_video_cnt',
                            'ft_app_ins_history_bank_cnt',
                            'ft_app_ins_history_cheating_cnt',
                            'ft_app_ins_history_child_rearin_cnt',
                            'ft_app_ins_history_credit_card_cnt',
                            'ft_app_ins_history_debit_credit_cnt',
                            'ft_app_ins_history_discounts_cnt',
                            'ft_app_ins_history_examination_cnt',
                            'ft_app_ins_history_finance_cnt',
                            'ft_app_ins_history_fitness_cnt',
                            'ft_app_ins_history_gamble_cnt',
                            'ft_app_ins_history_game_cnt',
                            'ft_app_ins_history_gpscheat_cnt',
                            'ft_app_ins_history_imei_alter_cnt',
                            'ft_app_ins_history_insurance_cnt',
                            'ft_app_ins_history_invest_cnt',
                            'ft_app_ins_history_life_casual_cnt',
                            'ft_app_ins_history_live_cnt',
                            'ft_app_ins_history_lottery_cnt',
                            'ft_app_ins_history_malicious_cnt',
                            'ft_app_ins_history_market_cnt',
                            'ft_app_ins_history_messaging_social_cnt',
                            'ft_app_ins_history_micro_loan_cnt',
                            'ft_app_ins_history_money_management_cnt',
                            'ft_app_ins_history_news_reading_cnt',
                            'ft_app_ins_history_office_business_cnt',
                            'ft_app_ins_history_online_gamble_cnt',
                            'ft_app_ins_history_online_shopping_cnt',
                            'ft_app_ins_history_payment_cnt',
                            'ft_app_ins_history_photo_cnt',
                            'ft_app_ins_history_risk_cnt',
                            'ft_app_ins_history_short_video_cnt',
                            'ft_app_ins_history_simulator_cnt',
                            'ft_app_ins_history_tally_cnt',
                            'ft_app_ins_history_travel_cnt',
                            'ft_app_ins_history_video_cnt',
                            'ft_dev_battery_all_30d_whole_allday_hours',
                            'ft_dev_battery_all_90d_whole_allday_hours',
                            'ft_dev_battery_charge_30d_weekday_allday_hours',
                            'ft_dev_battery_charge_30d_weekend_allday_hours',
                            'ft_dev_battery_charge_30d_whole_allday_hours',
                            'ft_dev_battery_charge_90d_weekday_allday_hours',
                            'ft_dev_battery_charge_90d_weekend_allday_hours',
                            'ft_dev_battery_charge_90d_whole_allday_hours',
                            'ft_dev_battery_full_30d_weekday_allday_hours',
                            'ft_dev_battery_full_30d_weekend_allday_hours',
                            'ft_dev_battery_full_30d_whole_allday_hours',
                            'ft_dev_battery_full_90d_weekday_allday_hours',
                            'ft_dev_battery_full_90d_weekend_allday_hours',
                            'ft_dev_battery_full_90d_whole_allday_hours',
                            'ft_dev_battery_use_30d_weekday_allday_hours',
                            'ft_dev_battery_use_30d_weekday_closetime_hours',
                            'ft_dev_battery_use_30d_weekday_nighttime_hours',
                            'ft_dev_battery_use_30d_weekday_worktime_hours',
                            'ft_dev_battery_use_30d_weekend_allday_hours',
                            'ft_dev_battery_use_30d_whole_allday_hours',
                            'ft_dev_battery_use_30d_whole_closetime_hours',
                            'ft_dev_battery_use_30d_whole_nighttime_hours',
                            'ft_dev_battery_use_30d_whole_worktime_hours',
                            'ft_dev_battery_use_90d_weekday_allday_hours',
                            'ft_dev_battery_use_90d_weekday_closetime_hours',
                            'ft_dev_battery_use_90d_weekday_nighttime_hours',
                            'ft_dev_battery_use_90d_weekday_worktime_hours',
                            'ft_dev_battery_use_90d_weekend_allday_hours',
                            'ft_dev_battery_use_90d_whole_allday_hours',
                            'ft_dev_battery_use_90d_whole_closetime_hours',
                            'ft_dev_battery_use_90d_whole_nighttime_hours',
                            'ft_dev_battery_use_90d_whole_worktime_hours',
                            'ft_dev_ip_30d_weekday_allday_cnt',
                            'ft_dev_ip_30d_weekday_closetime_cnt',
                            'ft_dev_ip_30d_weekday_nighttime_cnt',
                            'ft_dev_ip_30d_weekday_worktime_cnt',
                            'ft_dev_ip_30d_weekend_allday_cnt',
                            'ft_dev_ip_30d_whole_allday_cnt',
                            'ft_dev_ip_30d_whole_closetime_cnt',
                            'ft_dev_ip_30d_whole_nighttime_cnt',
                            'ft_dev_ip_30d_whole_worktime_cnt',
                            'ft_dev_wifimac_30d_weekday_allday_days',
                            'ft_dev_wifimac_30d_weekday_allday_cnt',
                            'ft_dev_wifimac_30d_weekday_closetime_days',
                            'ft_dev_wifimac_30d_weekday_closetime_cnt',
                            'ft_dev_wifimac_30d_weekday_nighttime_days',
                            'ft_dev_wifimac_30d_weekday_nighttime_cnt',
                            'ft_dev_wifimac_30d_weekday_worktime_days',
                            'ft_dev_wifimac_30d_weekday_worktime_cnt',
                            'ft_dev_wifimac_30d_weekend_allday_days',
                            'ft_dev_wifimac_30d_weekend_allday_cnt',
                            'ft_dev_wifimac_30d_whole_allday_days',
                            'ft_dev_wifimac_30d_whole_allday_cnt',
                            'ft_dev_wifimac_30d_whole_closetime_days',
                            'ft_dev_wifimac_30d_whole_closetime_cnt',
                            'ft_dev_wifimac_30d_whole_nighttime_days',
                            'ft_dev_wifimac_30d_whole_nighttime_cnt',
                            'ft_dev_wifimac_30d_whole_worktime_days',
                            'ft_dev_wifimac_30d_whole_worktime_cnt',
                            'ft_act_cate_ls_160000',
                            'ft_andr_t1_most_interest_ls_021000',
                            'ft_app_install_category_160000',
                            'ft_app_uninstall_category_160000',
                            'ft_cross_act_160000_tag_0844',
                            'ft_cross_blackfriends_act_2w_cat_16000',
                            'ft_cross_blackfriends_tag_p2p',
                            'ft_cross_ins_credit_ins_largest_cate_cnt',
                            'ft_cross_ins_loan_tag_business_travel',
                            'ft_cross_ins_loan_tag_p2p',
                            'ft_cross_ins_wifilocating_tag_credit_card',
                            'ft_cross_lbs_4wr_act_cnt_app_4w_unins',
                            'ft_cross_lbs_staycity_ins_160000',
                            'ft_cross_lbs_staycity_tag_021700',
                            'ft_cross_most_act_cate_lbs_staycity',
                            'ft_cross_tag_city_level1_housing_price',
                            'ft_cross_tag_city_level1_price',
                            'ft_cross_tag_city_level2_housing_price',
                            'ft_cross_tag_city_level2_price',
                            'ft_cross_tag_city_level3_housing_price',
                            'ft_cross_tag_city_level3_price',
                            'ft_cross_tag_city_level4_housing_price',
                            'ft_cross_tag_city_level4_price',
                            'ft_cross_tag_travel_macao_cnt',
                            'ft_cross_unins_app_ins_160000',
                            'ft_dev_all_nighter',
                            'ft_dev_deprecia_price',
                            'ft_dev_gid2imei_2w_cnt',
                            'ft_dev_gid2imsi_2w_cnt',
                            'ft_dev_gid2mac_2w_cnt',
                            'ft_dev_market_price',
                            'ft_dev_market_year',
                            'ft_dev_root',
                            'ft_dev_root_blacklist',
                            'ft_dev_timezone',
                            'ft_dev_trust',
                            'ft_dev_virtual',
                            'ft_dev_xposed',
                            'ft_gezhen_multi_loan_level',
                            'ft_gezhen_multi_loan_score',
                            'ft_gz_black_list',
                            'ft_gz_car_price',
                            'ft_gz_consumption_capacity',
                            'ft_gz_grey_list',
                            'ft_gz_housing_price_homeaddr_cnt',
                            'ft_gz_income_1',
                            'ft_gz_sensitive_area',
                            'ft_lbs_airport_4w_times',
                            'ft_lbs_entertainment_d_12w_days',
                            'ft_lbs_entertainment_f_12w_days',
                            'ft_lbs_entertainment_a_12w_days',
                            'ft_lbs_family_12w_change_cnt',
                            'ft_lbs_family_12w_cnt',
                            'ft_lbs_geo7_unusual',
                            'ft_lbs_hospital_12w_days',
                            'ft_lbs_hotel_4w_days',
                            'ft_lbs_hotel_4w_level',
                            'ft_lbs_house_price',
                            'ft_lbs_entertainment_b_12w_days',
                            'ft_lbs_entertainment_e_12w_days',
                            'ft_lbs_entertainment_c_12w_days',
                            'ft_lbs_property_fee',
                            'ft_lbs_same_night_stay_wifimac_cnt',
                            'ft_lbs_stable_stops',
                            'ft_lbs_trainstation_4w_times',
                            'ft_lbs_work_12w_change_cnt',
                            'ft_lbs_work_12w_cnt',
                            'ft_most_act_cate_ls_160000',
                            'ft_social_blackfriends',
                            'ft_social_blackfriends_group',
                            'ft_stable_imsi_active_days',
                            'ft_stable_imsi_changes',
                            'ft_stable_imsi_used_days',
                            'ft_tag_car_ownership',
                            'ft_tag_consumption_range',
                            'ft_tag_education',
                            'ft_tag_province',
                            'ft_tag_city',
                            'ft_dev_phone_brand',
                            'ft_dev_phone_model',
                            'ft_tag_age',
                            'ft_tag_asset_management',
                            'ft_tag_banking',
                            'ft_tag_bas_fraudster',
                            'ft_tag_bookkeeping',
                            'ft_tag_bourgeois',
                            'ft_tag_city_tier',
                            'ft_tag_consumption_level',
                            'ft_tag_credit_card',
                            'ft_tag_fitness',
                            'ft_tag_gender',
                            'ft_tag_health',
                            'ft_tag_hotel',
                            'ft_tag_industry_ad',
                            'ft_tag_industry_financial',
                            'ft_tag_industry_it',
                            'ft_tag_language_learing',
                            'ft_tag_lottery',
                            'ft_tag_marrige',
                            'ft_tag_occupation_entrepreneur',
                            'ft_tag_occupation_it',
                            'ft_tag_occupation_medical',
                            'ft_tag_occupation_teacher',
                            'ft_tag_online_learing',
                            'ft_tag_p2p',
                            'ft_tag_parent_0to2y',
                            'ft_tag_parent_3to6y',
                            'ft_tag_parent_k1tok6',
                            'ft_tag_parent_k7tok12',
                            'ft_tag_primary_purchaser',
                            'ft_tag_purchaser',
                            'ft_tag_residence',
                            'ft_tag_shopping',
                            'ft_tag_stock',
                            'ft_tag_travel',
                            'ft_tag_property_owner',
                            'ft_tag_occupation_office',
                            'parent',
                            'mother',
                            'ft_cross_tag_college_student_tag_p2p',
                            'ft_cross_tag_p2p_tag_lifeservice',
                            'ft_lbs_city_stay_oneday_cnt',
                            'ft_lbs_city_stay_twoday_cnt',
                            'ft_act_2week_rest_active_period_ls_hour0_4',
                            'ft_act_2week_rest_active_period_ls_hour12_13',
                            'ft_act_2week_rest_active_period_ls_hour13_18',
                            'ft_act_2week_rest_active_period_ls_hour18_23',
                            'ft_act_2week_rest_active_period_ls_hour5_7',
                            'ft_act_2week_rest_active_period_ls_hour8_11',
                            'ft_act_2week_work_active_period_ls_hour0_4',
                            'ft_act_2week_work_active_period_ls_hour12_13',
                            'ft_act_2week_work_active_period_ls_hour13_18',
                            'ft_act_2week_work_active_period_ls_hour18_23',
                            'ft_act_2week_work_active_period_ls_hour5_7',
                            'ft_act_2week_work_active_period_ls_hour8_11',
                            'ft_act_2week_rest_less_act_times',
                            'ft_act_2week_rest_most_act_times',
                            'ft_act_2week_rest_sum_act_times',
                            'ft_act_2week_work_less_act_times',
                            'ft_act_2week_work_most_act_times',
                            'ft_act_2week_work_sum_act_times',
                            'ft_act_2week_rest_less_act_period_ls_hour12_13',
                            'ft_act_2week_rest_less_act_period_ls_hour5_7',
                            'ft_act_2week_rest_most_act_period_ls_hour13_18',
                            'ft_act_2week_rest_most_act_period_ls_hour18_23',
                            'ft_act_2week_rest_most_act_period_ls_hour8_11',
                            'ft_act_2week_work_most_act_period_ls_hour13_18',
                            'ft_act_2week_work_most_act_period_ls_hour18_23',
                            'ft_act_2week_work_most_act_period_ls_hour8_11',
                            'ft_act_cate_ls_100000',
                            'ft_act_cate_ls_120000',
                            'ft_act_cate_ls_140000',
                            'ft_act_cate_ls_150000',
                            'ft_act_cate_ls_200000',
                            'ft_act_cate_ls_210000',
                            'ft_act_cate_ls_220000',
                            'ft_act_cate_ls_230000',
                            'ft_act_cate_ls_240000',
                            'ft_act_cate_ls_270000',
                            'ft_act_cate_ls_300000',
                            'ft_act_cate_num',
                            'ft_act_max_act_time',
                            'ft_act_month_rest_active_period_ls_hour0_4',
                            'ft_act_month_rest_active_period_ls_hour12_13',
                            'ft_act_month_rest_active_period_ls_hour13_18',
                            'ft_act_month_rest_active_period_ls_hour18_23',
                            'ft_act_month_rest_active_period_ls_hour5_7',
                            'ft_act_month_rest_active_period_ls_hour8_11',
                            'ft_act_month_rest_less_act_period_ls_hour0_4',
                            'ft_act_month_rest_less_act_period_ls_hour12_13',
                            'ft_act_month_rest_less_act_period_ls_hour5_7',
                            'ft_act_month_rest_less_act_times',
                            'ft_act_month_rest_most_act_period_ls_hour13_18',
                            'ft_act_month_rest_most_act_period_ls_hour18_23',
                            'ft_act_month_rest_most_act_period_ls_hour8_11',
                            'ft_act_month_rest_most_act_times',
                            'ft_act_month_rest_sum_act_times',
                            'ft_act_month_work_active_period_ls_hour0_4',
                            'ft_act_month_work_active_period_ls_hour8_11',
                            'ft_act_month_work_active_period_ls_hour12_13',
                            'ft_act_month_work_active_period_ls_hour13_18',
                            'ft_act_month_work_active_period_ls_hour18_23',
                            'ft_act_month_work_active_period_ls_hour5_7',
                            'ft_act_month_work_less_act_period_ls_hour0_4',
                            'ft_act_month_work_less_act_period_ls_hour12_13',
                            'ft_act_month_work_less_act_period_ls_hour5_7',
                            'ft_act_month_work_less_act_period_ls_hour8_11',
                            'ft_act_month_work_less_act_times',
                            'ft_act_month_work_most_act_period_ls_hour13_18',
                            'ft_act_month_work_most_act_period_ls_hour18_23',
                            'ft_act_month_work_most_act_period_ls_hour8_11',
                            'ft_act_month_work_most_act_times',
                            'ft_act_month_work_sum_act_times',
                            'ft_act_pkg_num',
                            'ft_ins_cate_app_cnt_ls_100000',
                            'ft_ins_cate_app_cnt_ls_120000',
                            'ft_ins_cate_app_cnt_ls_130000',
                            'ft_ins_cate_app_cnt_ls_140000',
                            'ft_ins_cate_app_cnt_ls_150000',
                            'ft_ins_cate_app_cnt_ls_160000',
                            'ft_ins_cate_app_cnt_ls_170000',
                            'ft_ins_cate_app_cnt_ls_190000',
                            'ft_ins_cate_app_cnt_ls_200000',
                            'ft_ins_cate_app_cnt_ls_210000',
                            'ft_ins_cate_app_cnt_ls_220000',
                            'ft_ins_cate_app_cnt_ls_230000',
                            'ft_ins_cate_app_cnt_ls_240000',
                            'ft_ins_cate_app_cnt_ls_250000',
                            'ft_ins_cate_app_cnt_ls_270000',
                            'ft_ins_cate_app_cnt_ls_290000',
                            'ft_ins_cate_app_cnt_ls_300000',
                            'ft_ins_cate_app_cnt_ls_900400',
                            'ft_ins_cate_app_cnt_ls_900500',
                            'ft_ins_cate_app_cnt_ls_900600',
                            'ft_ins_cate_app_cnt_ls_900700',
                            'ft_ins_category_cnt',
                            'ft_ins_app_install_category_160000',
                            'ft_ins_app_uninstall_category_120000',
                            'ft_ins_app_uninstall_category_140000',
                            'ft_ins_app_uninstall_category_150000',
                            'ft_ins_app_uninstall_category_160000',
                            'ft_ins_app_uninstall_category_190000',
                            'ft_ins_app_uninstall_category_200000',
                            'ft_ins_app_uninstall_category_210000',
                            'ft_ins_app_uninstall_category_230000',
                            'ft_ins_app_uninstall_category_240000',
                            'ft_ins_app_uninstall_category_270000',
                            'ft_ins_app_uninstall_category_300000',
                            'ft_ins_app_uninstall_category_900400',
                            'ft_ins_largest_cate_ls_120000',
                            'ft_ins_largest_cate_ls_140000',
                            'ft_ins_largest_cate_ls_150000',
                            'ft_ins_largest_cate_ls_190000',
                            'ft_ins_largest_cate_ls_200000',
                            'ft_ins_largest_cate_ls_210000',
                            'ft_ins_largest_cate_ls_270000',
                            'ft_ins_largest_cate_cnt',
                            'ft_ins_pkg_cnt',
                            'ft_lbs_home_cons_ls_high',
                            'ft_lbs_home_cons_ls_low',
                            'ft_lbs_home_cons_ls_middle',
                            'ft_lbs_pwoi_all_mostoften_consume_high',
                            'ft_lbs_pwoi_all_mostoften_consume_low',
                            'ft_lbs_pwoi_all_mostoften_consume_middle',
                            'ft_lbs_pwoi_all_often_consum_high',
                            'ft_lbs_pwoi_all_often_consum_low',
                            'ft_lbs_pwoi_all_often_consum_middle',
                            'ft_lbs_work_cons_ls_high',
                            'ft_lbs_work_cons_ls_low',
                            'ft_lbs_work_cons_ls_middle',
                            'ft_lbs_dis_label',
                            'ft_lbs_residence_stability',
                            'ft_lbs_workplace_stability',
                            'ft_dev_storage',
                            'ft_dev_free_storage',
                            'ft_dev_storage_usage_ratio',
                            'ft_app_ins_history_shortterm_loan',
                            'ft_app_ins_current_shortterm_loan',
                            'ft_app_ins_current_finance_cnt_diff_m_lm',
                            'ft_app_ins_current_debit_credit_cnt_diff_m_lm',
                            'ft_app_ins_current_micro_loan_cnt_diff_m_lm',
                            'ft_app_act_30d_finance_cnt_diff_m_lm',
                            'ft_app_act_30d_finance_times_diff_m_lm',
                            'ft_app_act_30d_finance_days_diff_m_lm',
                            'ft_app_act_30d_debit_credit_cnt_diff_m_lm',
                            'ft_app_act_30d_debit_credit_times_diff_m_lm',
                            'ft_app_act_30d_debit_credit_days_diff_m_lm',
                            'ft_app_act_30d_micro_loan_cnt_diff_m_lm',
                            'ft_app_act_30d_micro_loan_times_diff_m_lm',
                            'ft_app_act_30d_micro_loan_days_diff_m_lm',
                            'ft_app_ins_current_finance_cnt_diff_m_llm',
                            'ft_app_ins_current_debit_credit_cnt_diff_m_llm',
                            'ft_app_ins_current_micro_loan_cnt_diff_m_llm',
                            'ft_app_act_30d_finance_cnt_diff_m_llm',
                            'ft_app_act_30d_finance_times_diff_m_llm',
                            'ft_app_act_30d_finance_days_diff_m_llm',
                            'ft_app_act_30d_debit_credit_cnt_diff_m_llm',
                            'ft_app_act_30d_debit_credit_times_diff_m_llm',
                            'ft_app_act_30d_debit_credit_days_diff_m_llm',
                            'ft_app_act_30d_micro_loan_cnt_diff_m_llm',
                            'ft_app_act_30d_micro_loan_times_diff_m_llm',
                            'ft_app_act_30d_micro_loan_days_diff_m_llm',
                            'ft_app_ins_current_finance_cnt_change',
                            'ft_app_ins_current_debit_credit_cnt_change',
                            'ft_app_ins_current_micro_loan_cnt_change',
                            'ft_app_act_30d_finance_cnt_change',
                            'ft_app_act_30d_finance_times_change',
                            'ft_app_act_30d_finance_days_change',
                            'ft_app_act_30d_debit_credit_cnt_change',
                            'ft_app_act_30d_debit_credit_times_change',
                            'ft_app_act_30d_debit_credit_days_change',
                            'ft_app_act_30d_micro_loan_cnt_change',
                            'ft_app_act_30d_micro_loan_times_change',
                            'ft_app_act_30d_micro_loan_days_change',
                            'ft_app_ins_current_finance_cnt_std',
                            'ft_app_ins_current_debit_credit_cnt_std',
                            'ft_app_ins_current_micro_loan_cnt_std',
                            'ft_app_act_30d_finance_cnt_std',
                            'ft_app_act_30d_finance_times_std',
                            'ft_app_act_30d_finance_days_std',
                            'ft_app_act_30d_debit_credit_cnt_std',
                            'ft_app_act_30d_debit_credit_times_std',
                            'ft_app_act_30d_debit_credit_days_std',
                            'ft_app_act_30d_micro_loan_cnt_std',
                            'ft_app_act_30d_micro_loan_times_std',
                            'ft_app_act_30d_micro_loan_days_std',
                            'ft_app_ins_current_finance_cnt_avg',
                            'ft_app_ins_current_debit_credit_cnt_avg',
                            'ft_app_ins_current_micro_loan_cnt_avg',
                            'ft_app_act_30d_finance_cnt_avg',
                            'ft_app_act_30d_finance_times_avg',
                            'ft_app_act_30d_finance_days_avg',
                            'ft_app_act_30d_debit_credit_cnt_avg',
                            'ft_app_act_30d_debit_credit_times_avg',
                            'ft_app_act_30d_debit_credit_days_avg',
                            'ft_app_act_30d_micro_loan_cnt_avg',
                            'ft_app_act_30d_micro_loan_times_avg',
                            'ft_app_act_30d_micro_loan_days_avg',
                            'ft_app_ins_current_finance_cnt_m_rate',
                            'ft_app_ins_current_debit_credit_cnt_m_rate',
                            'ft_app_ins_current_micro_loan_cnt_m_rate',
                            'ft_app_act_30d_finance_cnt_m_rate',
                            'ft_app_act_30d_finance_times_m_rate',
                            'ft_app_act_30d_finance_days_m_rate',
                            'ft_app_act_30d_debit_credit_cnt_m_rate',
                            'ft_app_act_30d_debit_credit_times_m_rate',
                            'ft_app_act_30d_debit_credit_days_m_rate',
                            'ft_app_act_30d_micro_loan_cnt_m_rate',
                            'ft_app_act_30d_micro_loan_times_m_rate',
                            'ft_app_act_30d_micro_loan_days_m_rate',
                            'ft_app_ins_current_finance_cnt_cv',
                            'ft_app_ins_current_debit_credit_cnt_cv',
                            'ft_app_ins_current_micro_loan_cnt_cv',
                            'ft_app_act_30d_finance_cnt_cv',
                            'ft_app_act_30d_finance_times_cv',
                            'ft_app_act_30d_finance_days_cv',
                            'ft_app_act_30d_debit_credit_cnt_cv',
                            'ft_app_act_30d_debit_credit_times_cv',
                            'ft_app_act_30d_debit_credit_days_cv',
                            'ft_app_act_30d_micro_loan_cnt_cv',
                            'ft_app_act_30d_micro_loan_times_cv',
                            'ft_app_act_30d_micro_loan_days_cv',
                            'ft_stable_score_a',
                            'ft_asset_score_a',
                            'ft_consumption_score_a',
                            'ft_stable_score_c',
                            'ft_asset_score_c',
                            'ft_consumption_score_c',
                            'ft_safe_score_c',
                            'ft_finance_score_c',
                            'ft_stable_score_e',
                            'ft_consumption_score_e',
                            'ft_asset_score_e',
                            'ft_safe_score_e',
                            'ft_finance_score_e',
                            'ft_stable_score_b',
                            'ft_asset_score_b',
                            'ft_consumption_score_b',
                            'ft_stable_score_d',
                            'ft_asset_score_d',
                            'ft_consumption_score_d',
                            'ft_safe_score_d',
                            'ft_finance_score_d',
                            'ft_stable_score_f',
                            'ft_asset_score_f',
                            'ft_consumption_score_f',
                            'ft_safe_score_f',
                            'ft_finance_score_f']


    def get_sql(self):
        sql = "select gid, ###"
        for col in self.all_columns:
            if col in self.blacklist_var:
                sql = sql + "(case when {}='' then 'blank' else 1 end) as {}, ###".format(col, col)
            elif col in self.class_var:
                sql = sql + "(case when {}='' then 'blank' else {} end) as {}, ###".format(col, col, col)
            else:
                tmp_config = self.config_df[self.config_df.feature == col]
                tmp_config = tmp_config.reset_index(drop=True)
                sql = sql + "(case when {}='' then 'blank'".format(col)
                for index, row in tmp_config.iterrows():
                    if index == 0:
                        sql = sql + " when float({})<={} then '{}'".format(row['feature'], row['max_value'], row['tag'])
                    elif index == len(tmp_config) - 1:
                        sql = sql + " when float({})>{} then '{}'".format(row['feature'], row['min_value'], row['tag'])
                    else:
                        sql = sql + " when float({})<={} and float({})>{} then '{}'".format(row['feature'], row['max_value'], row['feature'], row['min_value'], row['tag'])
                sql = sql + "end) as {}, ###".format(col)
        return sql


d2t = Data2Tag()
sql = d2t.get_sql()
