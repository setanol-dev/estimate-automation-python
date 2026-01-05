# Estimate Automation Tool (Python)

## Overview
This project is a Python-based business automation tool that generates estimates
from CSV input files and outputs formatted documents automatically.

## Problem
Manual estimation using Excel is time-consuming and error-prone.

## Solution
This tool automates:
- CSV-based input
- Rule-based calculation
- Automatic document generation
- Simple logging

## Target Users
- Small manufacturing teams
- Back-office staff
- Engineers handling repetitive estimation tasks

## Status
Work in progress

## Workflow Design
【Input】
- CSVファイル（見積元データ）
- カラム構成：
  - item_name：品名
  - quantity：数量（整数）
  - unit_price：単価（数値）
  - rush_flag：特急対応（0 or 1）
  - discount_rate：割引率（0.0〜0.3）

【Process】
- CSVファイルを読み込む
- 各行について以下を実施
  - quantity × unit_price で小計を算出
  - rush_flag = 1 の場合、小計に10%加算
  - discount_rate が指定されている場合、割引適用
- 全行の金額を合算し、合計金額を算出
- 見積番号を「EST-YYYYMMDD-連番」で自動生成
- 実行日時を記録
- エラー行があれば処理ログに記録

【Output】
- 見積結果をまとめたExcelファイル
- ファイル名：estimate_YYYYMMDD.xlsx
- 出力先：sample_output フォルダ
- 処理ログ（テキスト）
