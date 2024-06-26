import frappe

@frappe.whitelist(allow_guest=True)
def create_doctype():
    try:
        doctypes = [
            {
                "name": "Property Document",
                "child_table": 1,
                "fields": {
                    "field1": {
                        "fieldname": "document_id",
                        "fieldtype": "Data",
                        "label": "Document ID",
                        "reqd": 1,
                        "unique": 1
                    },
                    "field2": {
                        "fieldname": "document_name",
                        "fieldtype": "Data",
                        "label": "Document Name",
                        "reqd": 1
                    },
                    "field3": {
                        "fieldname": "document_type",
                        "fieldtype": "Select",
                        "label": "Document Type",
                        "options": "Ownership\nTax\nOther",
                        "reqd": 1
                    },
                    "field4": {
                        "fieldname": "document_file",
                        "fieldtype": "Attach",
                        "label": "Document File"
                    },
                    "field5": {
                        "fieldname": "document_description",
                        "fieldtype": "Text",
                        "label": "Document Description"
                    }
                }
            },
            {
                "name": "Unit",
                "child_table": 0,
                "fields": {
                 "field1":  {
                           "fieldname": "unit_name",
                           "fieldtype": "Data",
                           "label": "Unit Name",
                            "reqd": 1
                  },
                 "field2":  {
                           "fieldname": "description",
                           "fieldtype": "Text Editor",
                           "label": "Description"
                  },
                 "field3":  {
                           "fieldname": "active",
                           "fieldtype": "Check",
                           "label": "Active",
                           "default": 1
                  }
                }
            },
            {
                "name": "Contaminants Detected Table",
                "child_table": 1,
                "fields": {
                  "field1":  {
                            "fieldname": "contaminant",
                            "fieldtype": "Data",
                            "label": "Contaminant",
                            "reqd": 1
                   },
                  "field2":  {
                            "fieldname": "quantity",
                            "fieldtype": "Float",
                            "label": "Quantity",
                            "reqd": 1
                   },
                  "field3":  {
                            "fieldname": "unit",
                            "fieldtype": "Link",
                            "label": "Unit",
                            "options": "Unit",
                            "reqd": 1
                 }
                }
            },
            {
                "name": "Property",
                "child_table": 0,
                "fields": {
                    "field1": {
                        "fieldname": "property_id",
                        "fieldtype": "Data",
                        "label": "Property ID",
                        "reqd": 1,
                        "unique": 1
                    },
                    "field2": {
                        "fieldname": "property_address",
                        "fieldtype": "Text",
                        "label": "Property Address",
                        "reqd": 1
                    },
                    "field3": {
                        "fieldname": "property_owner",
                        "fieldtype": "Link",
                        "label": "Property Owner",
                        "options": "User",
                        "reqd": 1
                    },
                    "field4": {
                        "fieldname": "property_type",
                        "fieldtype": "Select",
                        "label": "Property Type",
                        "options": "Residential\nCommercial\nIndustrial\nAgricultural",
                        "reqd": 1
                    },
                    "field5": {
                        "fieldname": "property_status",
                        "fieldtype": "Select",
                        "label": "Property Status",
                        "options": "Active\nInactive",
                        "reqd": 1
                    },
                    "field6": {
                        "fieldname": "property_tax",
                        "fieldtype": "Currency",
                        "label": "Property Tax",
                        "reqd": 1
                    },
                    "field7": {
                        "fieldname": "property_area",
                        "fieldtype": "Float",
                        "label": "Property Area (Sq. Ft.)",
                        "reqd": 1
                    },
                    "field8": {
                        "fieldname": "property_documents",
                        "fieldtype": "Table",
                        "label": "Property Documents",
                        "options": "Property Document"
                    }
                }
            },
            {
                "name": "No Dues Certificate",
                "child_table": 0,
                "fields": {
                "field1":  {
                        "fieldname": "certificate_id",
                        "fieldtype": "Data",
                        "label": "Certificate ID",
                         "reqd": 1,
                         "unique": 1
                    },
                  "field2": {
                           "fieldname": "issue_date",
                           "fieldtype": "Date",
                            "label": "Issue Date",
                            "reqd": 1
                   },
                  "field3": {
                           "fieldname": "valid_till",
                           "fieldtype": "Date",
                           "label": "Valid Till",
                           "reqd": 1
                  },
                  "field4": {
                           "fieldname": "certificate_status",
                            "fieldtype": "Select",
                             "label": "Certificate Status",
                             "options": "Active\nExpired",
                             "reqd": 1
                  },
                 "field5": {
                           "fieldname": "certificate_document",
                             "fieldtype": "Attach",
                              "label": "Certificate Document"
                 }
                }
            },
             {
                "name": "Property Tax",
                "child_table": 0,
                "fields": {
                "field1":  {
                          "fieldname": "tax_id",
                          "fieldtype": "Data",
                          "label": "Tax ID",
                          "reqd": 1,
                          "unique": 1
                  },
                  "field2": {
                            "fieldname": "tax_year",
                            "fieldtype": "Int",
                            "label": "Tax Year",
                             "reqd": 1
                 },
                  "field3":  {
                            "fieldname": "tax_amount",
                            "fieldtype": "Currency",
                            "label": "Tax Amount",
                            "reqd": 1
                 },
                  "field4": {
                           "fieldname": "tax_status",
                           "fieldtype": "Select",
                           "label": "Tax Status",
                           "options": "Unpaid\nPaid\nOverdue",
                           "reqd": 1
               },
                 "field5":  {
                            "fieldname": "payment_date",
                            "fieldtype": "Date",
                            "label": "Payment Date",
                            "depends_on": "eval:doc.tax_status == 'Paid'"
                 },
                 "field6":  {
                            "fieldname": "payment_receipt",
                            "fieldtype": "Attach",
                            "label": "Payment Receipt",
                            "depends_on": "eval:doc.tax_status == 'Paid'"
                 }
                }
            },
            {
                "name": "Property Tax Assessment",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "assessment_id",
                           "fieldtype": "Data",
                           "label": "Assessment ID",
                            "reqd": 1,
                            "unique": 1
                  },
                  "field2":  {
                             "fieldname": "assessment_date",
                             "fieldtype": "Date",
                             "label": "Assessment Date",
                             "reqd": 1
                  },
                  "field3":  {
                             "fieldname": "assessment_value",
                             "fieldtype": "Currency",
                             "label": "Assessed Value",
                             "reqd": 1
                  },
                  "field4": {
                            "fieldname": "tax_rate",
                            "fieldtype": "Percent",
                             "label": "Tax Rate",
                             "reqd": 1
                 },
                 "field5":  {
                             "fieldname": "tax_due",
                             "fieldtype": "Currency",
                             "label": "Tax Due",
                             "reqd": 1
                 },
                 "field6":   {
                             "fieldname": "payment_status",
                              "fieldtype": "Select",
                              "label": "Payment Status",
                              "options": "Unpaid\nPaid",
                              "reqd": 1
                }
               }
            },
             {
                "name": "Property Owner",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "owner_name",
                            "fieldtype": "Data",
                            "label": "Owner Name"
                  },              
                  "field2":  {
                             "fieldname": "contact_information",
                             "fieldtype": "Data",
                             "label": "Contact Information"
                  },
                  "field3":  {
                            "fieldname": "property_link",
                            "fieldtype": "Link",
                            "label": "Property",
                            "options": "Property"
                }
               }
            },
            {
                "name": "Property Documents",
                "child_table": 0,
                "fields": {
                "field1":   {
                            "fieldname": "property_id",
                            "fieldtype": "Link",
                            "label": "Property ID",
                            "options": "Property"
                  },
                  "field2":  {
                             "fieldname": "document_type",
                             "fieldtype": "Select",
                             "label": "Document Type",
                             "options": "Property Tax Receipt\nNo Dues Certificate\nProperty Registration Document\nOthers"
                  },
                  "field3":  {
                             "fieldname": "document_file",
                              "fieldtype": "Attach",
                              "label": "Document File"
                  },
                 "field4":  {
                            "fieldname": "issue_date",
                            "fieldtype": "Date",
                            "label": "Issue Date"
                 },
                 "field5":  {
                            "fieldname": "expiry_date",
                            "fieldtype": "Date",
                            "label": "Expiry Date"
                 }
             
               }
            },
            {
                "name": "Property Transfer History",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "property_id",
                           "fieldtype": "Link",
                           "label": "Property ID",
                           "options": "Property"
                  },
                  "field2":  {
                             "fieldname": "transfer_date",
                             "fieldtype": "Date",
                             "label": "Transfer Date"
                   },
                  "field3":  {
                             "fieldname": "previous_owner",
                             "fieldtype": "Data",
                             "label": "Previous Owner"
                  },
                 "field4":  {
                            "fieldname": "new_owner",
                            "fieldtype": "Data",
                            "label": "New Owner"
                  },
                 "field5":  {
                            "fieldname": "transfer_document",
                            "fieldtype": "Attach",
                            "label": "Transfer Document"
                 }
               }
            },
            {
                "name": "Property Maintenance",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "property_id",
                           "fieldtype": "Link",
                           "label": "Property ID",
                           "options": "Property"
                   },
                  "field2":  {
                            "fieldname": "maintenance_type",
                            "fieldtype": "Select",
                            "label": "Maintenance Type",
                            "options": "Plumbing\nElectrical\nStructural\nCleaning\nOther"
                   },
                  "field3":  {
                            "fieldname": "maintenance_date",
                            "fieldtype": "Date",
                            "label": "Maintenance Date"
                  },
                 "field4":  {
                           "fieldname": "description",
                           "fieldtype": "Text",
                           "label": "Description"
                  },
                 "field5":  {
                           "fieldname": "status",
                           "fieldtype": "Select",
                           "label": "Status",
                           "options": "Scheduled\nIn Progress\nCompleted"
                 },
                 "field6":  {
                             "fieldname": "cost",
                             "fieldtype": "Currency",
                             "label": "Cost"
                },
                 "field7":  {
                            "fieldname": "maintenance_document",
                            "fieldtype": "Attach",
                            "label": "Maintenance Document"
                }
               }
            },
            {
                "name": "Water Connection",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "property_id",
                           "fieldtype": "Link",
                           "label": "Property ID",
                           "options": "Property"
                  },
                  "field2": {
                            "fieldname": "connection_type",
                            "fieldtype": "Select",
                            "label": "Connection Type",
                            "options": "Residential\nCommercial\nIndustrial"
                  },
                  "field3":  {
                             "fieldname": "connection_status",
                              "fieldtype": "Select",
                              "label": "Connection Status",
                               "options": "Active\nInactive\nPending"
                  },
                 "field4":  {
                           "fieldname": "installation_date",
                           "fieldtype": "Date",
                           "label": "Installation Date"
                  },
                 "field5":  {
                           "fieldname": "meter_number",
                           "fieldtype": "Data",
                           "label": "Meter Number"
                 },
                 "field6":  {
                           "fieldname": "meter_reading",
                           "fieldtype": "Int",
                           "label": "Meter Reading"
                  }
                 
               }
            },
            {
                "name": "Water Usage",
                "child_table": 0,
                "fields": {
                "field1":  {
                         "fieldname": "connection_id",
                         "fieldtype": "Link",
                         "label": "Connection ID",
                         "options": "Water Connection"
                     },
               "field2": {
                        "fieldname": "reading_date",
                        "fieldtype": "Date",
                        "label": "Reading Date"
                   },
               "field3": {
                        "fieldname": "previous_reading",
                        "fieldtype": "Int",
                        "label": "Previous Reading"
                  },
              "field4": {
                       "fieldname": "current_reading",
                       "fieldtype": "Int",
                       "label": "Current Reading"
                 },
             "field5": {
                     "fieldname": "usage",
                     "fieldtype": "Int",
                     "label": "Usage",
                     "formula": "current_reading - previous_reading"
               }
                 
               }
            },
            {
                "name": "Water Bill",
                "child_table": 0,
                "fields": {
                "field1": {
                          "fieldname": "bill_number",
                          "fieldtype": "Data",
                          "label": "Bill Number",
                          "unique": True
                  },
                "field2": {
                          "fieldname": "connection_id",
                          "fieldtype": "Link",
                          "label": "Connection ID",
                          "options": "Water Connection"
                 },
               "field3": {
                         "fieldname": "billing_period",
                         "fieldtype": "Data",
                         "label": "Billing Period"
                },
              "field4": {
                        "fieldname": "total_usage",
                        "fieldtype": "Int",
                        "label": "Total Usage"
               },
             "field5": {
                       "fieldname": "bill_amount",
                       "fieldtype": "Currency",
                       "label": "Bill Amount"
              },
            "field6": {
                      "fieldname": "payment_status",
                      "fieldtype": "Select",
                      "label": "Payment Status",
                      "options": "Unpaid\nPaid"
             },
           "field7":  {
                     "fieldname": "due_date",
                     "fieldtype": "Date",
                    "label": "Due Date"
              }
                 
               }
            },
            {
                "name": "New Application",
                "child_table": 0,
                "fields": {
                  "field1": {
                            "fieldname": "application_number",
                            "fieldtype": "Data",
                            "label": "Application Number",
                             "unique": True
                   },
                  "field2": {
                            "fieldname": "applicant_name",
                            "fieldtype": "Data",
                            "label": "Applicant Name"
                  },
                 "field3":  {
                           "fieldname": "property_id",
                           "fieldtype": "Link",
                           "label": "Property ID",
                           "options": "Property"
                  },
                 "field4":  {
                            "fieldname": "contact_number",
                            "fieldtype": "Data",
                            "label": "Contact Number"
                 },
                "field5":  {
                          "fieldname": "application_status",
                           "fieldtype": "Select",
                          "label": "Application Status",
                            "options": "Pending\nApproved\nRejected"
                },
              "field6":  {
                         "fieldname": "application_date",
                          "fieldtype": "Date",
                          "label": "Application Date"
                  }
                 
               }
            },
            {
                "name": "Application Status Tracking",
                "child_table": 0,
                "fields": {
                "field1":  {
                          "fieldname": "application_number",
                          "fieldtype": "Link",
                           "label": "Application Number",
                          "options": "New Application"
                },
               "field2":  {
                          "fieldname": "applicant_name",
                          "fieldtype": "Data",
                          "label": "Applicant Name",
                           "read_only":True
                },
              "field3":  {
                        "fieldname": "application_status",
                        "fieldtype": "Select",
                        "label": "Application Status",
                        "options": "Pending\nApproved\nRejected",
                        "read_only": True
                },
              "field4":  {
                        "fieldname": "application_date",
                        "fieldtype": "Date",
                        "label": "Application Date",
                        "read_only": True
               },
             "field5":  {
                       "fieldname": "last_update",
                       "fieldtype": "Datetime",
                       "label": "Last Status Update",
                        "read_only": True
                }
               }
            },
            {
                "name": "Water Quality Report",
                "child_table": 0,
                "fields": {
                 "field1": {
                          "fieldname": "report_id",
                          "fieldtype": "Data",
                          "label": "Report ID",
                          "reqd": 1,
                          "unique": 1
                   },
                  "field2": {
                           "fieldtype": "Date",
                           "label": "Date of Test",
                            "reqd": 1
                   },
                  "field3": {
                           "fieldname": "location_of_test",
                           "fieldtype": "Data",
                           "label": "Location of Test",
                           "reqd": 1
                  },
                 "field4":  {
                           "fieldname": "water_quality_index",
                           "fieldtype": "Float",
                           "label": "Water Quality Index",
                           "reqd": 1
                  },
                 "field5":  {
                           "fieldname": "contaminants_detected",
                           "fieldtype": "Table",
                           "label": "Contaminants Detected",
                           "options": "Contaminants Detected Table",
                           "reqd": 0
                 }
               }
            },
             {
                "name": "Water Supply Schedule",
                "child_table": 0,
                "fields": {
                 "field1":  {
                           "fieldname": "day_of_week",
                           "fieldtype": "Select",
                           "label": "Day of the Week",
                            "options": "Sunday\nMonday\nTuesday\nWednesday\nThursday\nFriday\nSaturday",
                             "reqd": 1
                    },
                  "field5":  {
                            "fieldname": "start_time",
                            "fieldtype": "Time",
                            "label": "Start Time",
                            "reqd": 1
                   },
                 "field5":   {
                            "fieldname": "end_time",
                            "fieldtype": "Time",
                            "label": "End Time",
                            "reqd": 1
                  },
                 "field5":   {
                            "fieldname": "notes",
                            "fieldtype": "Text",
                            "label": "Notes"
                  }
               }
            },
            {
                "name": "Water Conservation Category",
                "child_table": 0,
                "fields": {
                  "field1":  {
                             "fieldname": "category_name",
                              "fieldtype": "Data",
                              "label": "Category Name",
                              "reqd": 1
                    },
                  "field2":   {
                             "fieldname": "description",
                             "fieldtype": "Text Editor",
                             "label": "Description"
                    },
                  "field3":   {
                            "fieldname": "active",
                             "fieldtype": "Check",
                             "label": "Active",
                             "default": 1
                    }
               }
            },
            {
                "name": "Water Conservation Tips",
                "child_table": 0,
                "fields": {
                "field1":  {
                           "fieldname": "tip",
                           "fieldtype": "Text Editor",
                           "label": "Conservation Tip",
                           "reqd": 1
                  },
                 "field2": {
                          "fieldname": "category",
                          "fieldtype": "Link",
                         "label": "Category",
                         "options": "Water Conservation Category",
                         "reqd": 1
                  },
                "field3":  { 
                          "fieldname": "active",
                          "fieldtype": "Check",
                          "label": "Active",
                          "default": 1
                   }
               }
            },
            {
                "name": "Tariff Category",
                "child_table": 0,
                "fields": {
                "field1":   {
                           "fieldname": "tariff_category",
                           "fieldtype": "Data",
                           "label": "Tariff Category",
                            "reqd": 1,
                            "unique": 1
                  },
                "field2":  {
                          "fieldname": "description",
                          "fieldtype": "Text",
                          "label": "Description"
                  }
               
               }
            },
            {
                "name": "Water Tariff",
                "child_table": 0,
                "fields": {
                 "field1":  {
                            "fieldname": "tariff_category",
                            "fieldtype": "Link",
                            "label": "Tariff Category",
                            "options": "Tariff Category",
                              "reqd": 1
                   },
                  "field2":  {
                            "fieldname": "unit",
                            "fieldtype": "Link",
                            "label": "Unit",
                            "options": "Unit",
                            "reqd": 1
                    },
                   "field3":  {
                              "fieldname": "price_per_unit",
                              "fieldtype": "Currency",
                              "label": "Price Per Unit",
                               "reqd": 1
                    },
                   "field4":  {
                              "fieldname": "effective_from",
                                "fieldtype": "Date",
                               "label": "Effective From",
                               "reqd": 1
                    },
                   "field5":   {
                              "fieldname": "effective_until",
                              "fieldtype": "Date",
                              "label": "Effective Until"
                   }
                
               }
            },
             {
                "name": "Waste Management Account",
                "child_table": 0,
                "fields": {
                 "field1":   {
                            "fieldname": "account_number",
                            "fieldtype": "Data",
                            "label": "Account Number",
                              "reqd": 1,
                             "unique": 1
                    },
                  "field2":  {
                              "fieldname": "property_link",
                               "fieldtype": "Link",
                                "label": "Linked Property",
                                "reqd": 1,
                                "options": "Property"
                       },
                      "field3":  {
                                   "fieldname": "waste_management_type",
                                    "fieldtype": "Select",
                                    "label": "Waste Management Type",
                                     "reqd": 1,
                                      "options": "Residential\nCommercial"
                       },
                      "field4":   {
                                  "fieldname": "start_date",
                                  "fieldtype": "Date",
                                  "label": "Start Date",
                                   "reqd": 1
                        },
                      "field5":    {
                                  "fieldname": "end_date",
                                  "fieldtype": "Date",
                                  "label": "End Date"
                         },
                        "field6":  {
                                  "fieldname": "status",
                                  "fieldtype": "Select",
                                  "label": "Status",
                                   "reqd": 1,
                                   "options": "Active\nInactive"
                       }
                
               }
            },
            {
                "name": "Waste Collection Schedule",
                "child_table": 0,
                "fields": {
                 "field1":  {
                            "fieldname": "schedule_id",
                             "fieldtype": "Data",
                              "label": "Schedule ID",
                               "reqd": 1,
                                 "unique": 1
                    },
                   "field2":  {
                               "fieldname": "waste_management_account_link",
                                "fieldtype": "Link",
                                "label": "Linked Waste Management Account",
                                "reqd": 1,
                                "options": "Waste Management Account"
                     },
                    "field3":  {
                               "fieldname": "collection_frequency",
                               "fieldtype": "Select",
                                "label": "Collection Frequency",
                                "reqd": 1,
                                "options": "Daily\nBi-weekly\nWeekly\nMonthly"
                     },
                     "field4":  {
                               "fieldname": "next_collection_date",
                               "fieldtype": "Date",
                               "label": "Next Collection Date",
                               "reqd": 1
                     },
                    "field5":  {
                              "fieldname": "status",
                              "fieldtype": "Select",
                              "label": "Status",
                               "reqd": 1,
                               "options": "Active\nInactive"
                    }
                
               }
            },
             {
                "name": "Waste Collection Record",
                "child_table": 0,
                "fields": {
                 "field1":  {
                            "fieldname": "record_id",
                             "fieldtype": "Data",
                             "label": "Record ID",
                              "reqd": 1,
                              "unique": 1
                     },
                    "field2":  {
                               "fieldname": "schedule_link",
                               "fieldtype": "Link",
                               "label": "Linked Schedule",
                                "reqd": 1,
                                "options": "Waste Collection Schedule"
                     },
                    "field3":  {
                                "fieldname": "collection_date",
                                 "fieldtype": "Date",
                                 "label": "Collection Date",
                                   "reqd": 1
                      },
                     "field4":  {
                               "fieldname": "waste_collected",
                               "fieldtype": "Float",
                                "label": "Waste Collected (kg)",
                                "reqd": 1
                       },
                      "field5":  {
                                 "fieldname": "collection_status",
                                 "fieldtype": "Select",
                                 "label": "Collection Status",
                                 "reqd": 1,
                                  "options": "Collected\nNot Collected"
                      }
                
               }
            },
            {
                "name": "Waste Management Bill",
                "child_table": 0,
                "fields": {
                 "field1":  {
                            "fieldname": "bill_id",
                            "fieldtype": "Data",
                            "label": "Bill ID",
                             "reqd": 1,
                             "unique": 1
                     },
                    "field2":  {
                                "fieldname": "account_link",
                                "fieldtype": "Link",
                                "label": "Linked Account",
                                 "reqd": 1,
                                  "options": "Waste Management Account"
                    },
                    "field3":  {
                              "fieldname": "billing_period",
                              "fieldtype": "Data",
                               "label": "Billing Period",
                               "reqd": 1
                   },
                  "field4":  {
                             "fieldname": "total_amount",
                             "fieldtype": "Currency",
                              "label": "Total Amount",
                               "reqd": 1
                   },
                   "field5":  {
                             "fieldname": "payment_status",
                             "fieldtype": "Select",
                              "label": "Payment Status",
                              "reqd": 1,
                              "options": "Paid\nUnpaid"
                    },
                   "field6":    {
                              "fieldname": "due_date",
                              "fieldtype": "Date",
                             "label": "Due Date",
                              "reqd": 1
                   }
               }
            },
             {
                "name": "New SWM Application",
                "child_table": 0,
                "fields": {
                 "field1":    {
                             "fieldname": "application_id",
                              "fieldtype": "Data",
                              "label": "Application ID",
                               "reqd": 1,
                                "unique": 1
                    },
                   "field2":  { 
                             "fieldname": "applicant_name",
                              "fieldtype": "Data",
                              "label": "Applicant Name",
                               "reqd": 1
                     },
                    "field3":   {
                              "fieldname": "property_id",
                              "fieldtype": "Link",
                              "label": "Linked Property",
                              "reqd": 1,
                              "options": "Property"
                     },
                    "field6":   {
                               "fieldname": "application_date",
                               "fieldtype": "Date",
                               "label": "Application Date",
                                 "reqd": 1
                     },
                    "field4":    {
                                "fieldname": "status",
                                "fieldtype": "Select",
                                "label": "Application Status",
                                  "reqd": 1,
                                  "options": "Pending\nApproved\nRejected"
                      },
                     "field5":   {
                                "fieldname": "assigned_id",
                                "fieldtype": "Data",
                                  "label": "Assigned SWM ID",
                                    "reqd": 0
                      }
               }
            },
            {
                "name": "SWM Application Status Tracking",
                "child_table": 0,
                "fields": {
                  "field1":  {
                             "fieldname": "application_id",
                             "fieldtype": "Link",
                              "label": "Application ID",
                               "reqd": 1,
                               "options": "New SWM Application"
                      },
                     "field2":   {
                                "fieldname": "status",
                                "fieldtype": "Data",
                                "label": "Status",
                                  "reqd": 1
                        },
                       "field3":  {
                                 "fieldname": "date",
                                 "fieldtype": "Date",
                                 "label": "Status Date",
                                 "reqd": 1
                         },
                        "field4":  {
                                  "fieldname": "notes",
                                  "fieldtype": "Text",
                                  "label": "Notes",
                                    "reqd": 0
                       }
               }
            },
            {
                "name": "Waste Disposal Method",
                "child_table": 0,
                "fields": {
                  "field1":   {
                             "fieldname": "disposal_method",
                              "fieldtype": "Data",
                              "label": "Disposal Method",
                               "reqd": 1
                    },
                   "field2":   {
                               "fieldname": "description",
                                "fieldtype": "Text",
                                "label": "Description"
                   }
                 }
              },
               {
                "name": "Waste Type",
                "child_table": 0,
                "fields": {
                  "field1":   {
                             "fieldname": "waste_type",
                              "fieldtype": "Data",
                              "label": "Waste Type",
                               "reqd": 1
                    },
                   "field2":   {
                               "fieldname": "description",
                                "fieldtype": "Text",
                                "label": "Description"
                   }
                 }
              },
              {
                "name": "Waste Collection Vehicle",
                "child_table": 0,
                "fields": {
                 "field1":  {
                             "fieldname": "vehicle_id",
                             "fieldtype": "Data",
                             "label": "Vehicle ID",
                             "reqd": 1
                    },
                   "field2":  {
                             "fieldname": "vehicle_type",
                             "fieldtype": "Select",
                             "label": "Vehicle Type",
                             "options":"Truck\nVan\nBicycle",
                              "reqd": 1
                  },
                 "field3":   {
                            "fieldname": "capacity",
                            "fieldtype": "Int",
                            "label": "Capacity (in Kg)"
                 },
                "field4":   {
                           "fieldname": "operational_status",
                             "fieldtype": "Select",
                             "label": "Operational Status",
                             "options":"Operational\nUnder Maintenance\nOut of Service",
                             "reqd": 1
                   }
                 }
              },
                {
                "name": "Waste Processing Facility",
                "child_table": 0,
                "fields": {
                   "field1": {
                            "fieldname": "facility_id",
                            "fieldtype": "Data",
                            "label": "Facility ID",
                            "reqd": 1
                      },
                     "field2":  {
                               "fieldname": "facility_name",
                               "fieldtype": "Data",
                               "label": "Facility Name",
                                "reqd": 1
                      },
                     "field3":  {
                               "fieldname": "facility_type",
                               "fieldtype": "Select",
                                "label": "Facility Type",
                                 "options":"Composting\nIncineration\nRecycling\nLandfill",
                                 "reqd": 1
                     },
                    "field4":   {
                               "fieldname": "location",
                               "fieldtype": "Data",
                                "label": "Location"
                    },
                   "field5":    {
                               "fieldname": "capacity",
                               "fieldtype": "Int",
                               "label": "Capacity (in Tonnes)"
                   },
                  "field6":   {
                             "fieldname": "operational_status",
                             "fieldtype": "Select",
                             "label": "Operational Status",
                             "options":"Operational\nUnder Maintenance\nOut of Service",
                             "reqd": 1
                   }
                 }
              },
              {
                "name": "Recycling Program",
                "child_table": 0,
                "fields": {
                   "field1":    {
                               "fieldname": "program_id",
                               "fieldtype": "Data",
                               "label": "Program ID",
                               "reqd": 1
                      },
                     "field2":  {
                               "fieldname": "program_name",
                               "fieldtype": "Data",
                               "label": "Program Name",
                                "reqd": 1
                       },
                      "field3":    {
                                  "fieldname": "description",
                                  "fieldtype": "Text Editor",
                                   "label": "Description"
                      },
                     "field4":    {
                                 "fieldname": "start_date",
                                 "fieldtype": "Date",
                                  "label": "Start Date",
                                  "reqd": 1
                      },
                     "field5":   {
                                 "fieldname": "end_date",
                                 "fieldtype": "Date",
                                 "label": "End Date"
                     },
                    "field6":    {
                                "fieldname": "status",
                                "fieldtype": "Select",
                                "label": "Status",
                                "options": "Active\nInactive\nCompleted",
                                "reqd": 1
                   }
                 }
              },
              {
                "name": "Waste Management Regulations",
                "child_table": 0,
                "fields": {
                   "field1":  {
                             "fieldname": "regulation_id",
                             "fieldtype": "Data",
                              "label": "Regulation ID",
                              "reqd": 1
                     },
                    "field2":  {
                              "fieldname": "regulation_title",
                              "fieldtype": "Data",
                              "label": "Regulation Title",
                              "reqd": 1
                    },
                   "field3":   {
                              "fieldname": "description",
                              "fieldtype": "Text Editor",
                              "label": "Description"
                   },
                  "field4":   {
                             "fieldname": "effective_date",
                             "fieldtype": "Date",
                             "label": "Effective Date",
                             "reqd": 1
                   },
                  "field5":   {
                              "fieldname": "expiration_date",
                              "fieldtype": "Date",
                               "label": "Expiration Date"
                  },
                 "field6":    {
                             "fieldname": "status",
                             "fieldtype": "Select",
                             "label": "Status",
                             "options":"Active\nInactive\nExpired",
                             "reqd": 1
                   }
                 }
              },
               {
                "name": "Community Engagement",
                "child_table": 0,
                "fields": {
                    "field1":   {
                               "fieldname": "engagement_id",
                               "fieldtype": "Data",
                               "label": "Engagement ID",
                               "reqd":1
                       },
                       "field2":  {
                                 "fieldname": "engagement_title",
                                 "fieldtype": "Data",
                                 "label": "Engagement Title",
                                  "reqd": 1
                        },
                       "field3":   {
                                   "fieldname": "description",
                                   "fieldtype": "Text Editor",
                                   "label": "Description"
                        },
                       "field4":   {
                                  "fieldname": "start_date",
                                  "fieldtype": "Date",
                                  "label": "Start Date",
                                  "reqd":1
                       },
                      "field5":   {
                                 "fieldname": "end_date",
                                 "fieldtype": "Date",
                                 "label": "End Date"
                       },
                      "field6":   {
                                 "fieldname": "status",
                                 "fieldtype": "Select",
                                 "label": "Status",
                                  "options": "Upcoming\nOngoing\nCompleted",
                                  "reqd":1
                   }
                 }
              },
              {
                "name": "Penalties and Fines",
                "child_table": 0,
                "fields": {
                     "field1":  {
                                "fieldname": "penalty_id",
                                 "fieldtype": "Data",
                                 "label": "Penalty ID",
                                  "reqd":1
                       },
                       "field2":  {
                                 "fieldname": "offense",
                                 "fieldtype": "Data",
                                 "label": "Offense",
                                  "reqd": 1
                       },
                      "field3":   {
                                  "fieldname": "description",
                                  "fieldtype": "Text Editor",
                                  "label": "Description"
                      },
                     "field4":    {   
                                 "fieldname": "penalty_amount",
                                 "fieldtype": "Currency",
                                 "label": "Penalty Amount",
                                 "reqd": 1
                      },
                     "field5":    { 
                                 "fieldname": "fine_date",
                                 "fieldtype": "Date",
                                  "label": "Fine Date",
                                  "reqd":1
                      },
                     "field6":    {
                                  "fieldname": "paid",
                                  "fieldtype": "Check",
                                  "label": "Paid"
                    }
                 }
              },
             
              {
                "name": "Business Account",
                "child_table": 0,
                "fields": {
                      "field1":   {
                                   "fieldname": "business_id",
                                   "fieldtype": "Data",
                                   "label": "Business ID",
                                    "reqd": 1
                        },
                       "field2":  {
                                  "fieldname": "business_name",
                                  "fieldtype": "Data",
                                  "label": "Business Name",
                                   "reqd":1
                       },
                      "field3":   {
                                 "fieldname": "business_address",
                                 "fieldtype": "Data",
                                 "label": "Business Address",
                                  "reqd": 1
                      },
                     "field3":    {
                                 "fieldname": "business_type",
                                 "fieldtype": "Select",
                                 "label": "Business Type",
                                 "options": "Retail\nWholesale\nManufacturing\nService\nOther",
                                 "reqd": 1
                      },
                     "field4":    {
                                 "fieldname": "contact_person",
                                 "fieldtype": "Data",
                                 "label": "Contact Person"
                     },
                    "field5":    {
                                "fieldname": "contact_number",
                                "fieldtype": "Data",
                                "label": "Contact Number"
                    },
                   "field6":    {
                               "fieldname": "email_id",
                               "fieldtype": "Data",
                              "label": "Email ID"
                   }
                 }
              },
              {
                "name": "Trade License",
                "child_table": 0,
                "fields": {
                      "field1":  {
                                "fieldname": "license_number",
                                "fieldtype": "Data",
                                "label": "License Number",
                                 "reqd": 1
                     },
                    "field2":   {
                               "fieldname": "business_id",
                               "fieldtype": "Link",
                               "label": "Business ID",
                               "reqd":1,
                               "options": "Business Account"
                    },
                   "field3":   {
                              "fieldname": "issue_date",
                              "fieldtype": "Date",
                              "label": "Issue Date",
                              "reqd": 1
                    },
                   "field4":   {
                               "fieldname": "expiry_date",
                                "fieldtype": "Date",
                                "label": "Expiry Date",
                                "reqd": 1
                    },
                   "field5":   {
                              "fieldname": "status",
                              "fieldtype": "Select",
                              "label": "Status",
                             "options": "Active\nExpired\nRenewal Due",
                             "reqd": 1
                     }
                 }
              },
              {
                "name": "Hoarding Application",
                "child_table": 0,
                "fields": {
                    "field1":   {
                                "fieldname": "application_id",
                                "fieldtype": "Data",
                                "label": "Application ID",
                                "reqd": 1
                       },
                      "field2":   {
                                 "fieldname": "business_id",
                                 "fieldtype": "Link",
                                 "label": "Business ID",
                                 "options": "Business Account",
                                 "reqd": 1
                       },
                       "field3":  {
                                 "fieldname": "application_date",
                                 "fieldtype": "Date",
                                  "label": "Application Date",
                                  "reqd":1
                        },
                       "field4":   {
                                  "fieldname": "hoarding_location",
                                   "fieldtype": "Data",
                                  "label": "Hoarding Location",
                                   "reqd":1
                        },
                       "field5":  {
                                 "fieldname": "hoarding_size",
                                 "fieldtype": "Data",
                                 "label": "Hoarding Size",
                                  "reqd":1
                        },
                        "field6":  {
                                  "fieldname": "status",
                                  "fieldtype": "Select",
                                   "label": "Status",
                                   "options": "Pending\nApproved\nRejected",
                                   "reqd": 1
                      }
                 }
              },
               {
                "name": "Hoarding Payment",
                "child_table": 0,
                "fields": {
                  "field1": {
                           "fieldname": "payment_id",
                           "fieldtype": "Data",
                           "label": "Payment ID",
                            "reqd": 1
                  },
                 "field2": {
                          "fieldname": "hoarding_application_id",
                          "fieldtype": "Link",
                          "label": "Hoarding Application ID",
                          "options": "Hoarding Application",
                           "reqd": 1
                 },
                "field3":  {
                          "fieldname": "payment_date",
                          "fieldtype": "Date",
                          "label": "Payment Date",
                          "reqd": 1
               },
              "field4":   {
                         "fieldname": "payment_amount",
                         "fieldtype": "Currency",
                         "label": "Payment Amount",
                          "reqd":1
             },
            "field5":  {
                       "fieldname": "payment_status",
                       "fieldtype": "Select",
                       "label": "Payment Status",
                        "options": "Pending\nPaid\nFailed",
                        "reqd": 1
                  }
                 }
              },
              {
                "name": "Rental Property",
                "child_table": 0,
                "fields": {
                  "field1":  {
                            "fieldname": "property_id",
                            "fieldtype": "Data",
                            "label": "Property ID",
                             "reqd": 1
                   },
                  "field2":   {
                             "fieldname": "property_address",
                             "fieldtype": "Data",
                             "label": "Property Address",
                             "reqd": 1
                   },
                  "field3":    {
                              "fieldname": "property_type",
                              "fieldtype": "Select",
                              "label": "Property Type",
                               "options": "Residential\nCommercial\nIndustrial",
                               "reqd": 1
                  },
                 "field4":     {
                               "fieldname": "rental_amount",
                               "fieldtype": "Currency",
                               "label": "Rental Amount",
                                "reqd": 1
                  },
                 "field5":    {
                              "fieldname": "lease_start_date",
                              "fieldtype": "Date",
                              "label": "Lease Start Date",
                              "reqd": 1
                  },
                 "field6":   {
                            "fieldname": "lease_end_date",
                             "fieldtype": "Date",
                             "label": "Lease End Date",
                             "reqd":1
                 },
                "field7":    {
                             "fieldname": "tenant_name",
                             "fieldtype": "Data",
                             "label": "Tenant Name",
                              "reqd": 1
                },
               "field8":     {
                            "fieldname": "tenant_contact",
                            "fieldtype": "Data",
                            "label": "Tenant Contact",
                             "reqd": 1
                  }
                 }
              },
               {
                "name": "Trade Ledger Report",
                "child_table": 0,
                "fields": {
                  "field1":  {
                             "fieldname": "report_id",
                             "fieldtype": "Data",
                             "label": "Report ID",
                              "reqd": 1
                   },
                  "field2":  {
                            "fieldname": "account_id",
                            "fieldtype": "Link",
                             "label": "Account ID",
                            "options": "Business Account",
                              "reqd":1
                },
               "field3":    {
                            "fieldname": "start_date",
                            "fieldtype": "Date",
                            "label": "Start Date",
                            "reqd": 1
               },
              "field4":     {
                            "fieldname": "end_date",
                            "fieldtype": "Date",
                            "label": "End Date",
                             "reqd":1
              },
             "field5":   {
                        "fieldname": "total_revenue",
                        "fieldtype": "Currency",
                        "label": "Total Revenue",
                         "reqd": 1
               },
              "field6":  {
                        "fieldname": "total_expenses",
                        "fieldtype": "Currency",
                         "label": "Total Expenses",
                        "reqd": 1
              },
             "field7":   {
                        "fieldname": "net_profit",
                        "fieldtype": "Currency",
                        "label": "Net Profit",
                        "reqd": 1
                  }
                 }
              },
             
               {
                "name": "Business Inspection Report",
                "child_table": 0,
                "fields": {
                    "field1":  {
                              "fieldname": "inspection_date",
                              "fieldtype": "Date",
                              "label": "Inspection Date"
                     },
                    "field2": {
                             "fieldname": "business_id",
                             "fieldtype": "Link",
                             "label": "Business ID",
                             "options": "Business Account"
                   },
                  "field3":   {
                             "fieldname": "inspector_name",
                             "fieldtype": "Data",
                             "label": "Inspector Name"
                  },
                 "field4":   {
                            "fieldname": "inspection_result",
                             "fieldtype": "Select",
                            "label": "Inspection Result",
                            "options": "Passed\nFailed\nConditional Pass"
                },
               "field5":    {
                            "fieldname": "notes",
                            "fieldtype": "Text",
                            "label": "Notes"
                     }
                 }
              },
              {
                "name": "Business Permit",
                "child_table": 0,
                "fields": {
                  "field1": {
                           "fieldname": "permit_number",
                           "fieldtype": "Data",
                           "label": "Permit Number"
                  },
                 "field2": {
                          "fieldname": "business_id",
                          "fieldtype": "Link",
                          "label": "Business ID",
                          "options": "Business Account"
               },
              "field3":   {
                         "fieldname": "issue_date",
                         "fieldtype": "Date",
                         "label": "Issue Date"
             },
            "field4":   {
                        "fieldname": "expiry_date",
                        "fieldtype": "Date",
                        "label": "Expiry Date"
            },
           "field5":   {
                      "fieldname": "permit_type",
                      "fieldtype": "Select",
                       "label": "Permit Type",
                        "options": "Operating Permit\nBuilding Permit\nSignage Permit\nHealth Permit\nOther"
            },
           "field6":  {
                     "fieldname": "status",
                     "fieldtype": "Select",
                      "label": "Status",
                     "options": "Active\nExpired\nRevoked"
                   }
                 }
              },
              {
                "name": "Advertisement Tax",
                "child_table": 0,
                "fields": {
                   "field1":  {
                             "fieldname": "tax_id",
                             "fieldtype": "Data",
                             "label": "Tax ID"
                     },
                    "field2":  {
                              "fieldname": "business_id",
                              "fieldtype": "Link",
                              "label": "Business ID",
                              "options": "Business Account"
                    },
                   "field3":  {
                             "fieldname": "advertisement_type",
                             "fieldtype": "Select",
                             "label": "Advertisement Type",
                             "options": "Billboard\nOnline\nPrint\nBroadcast\nDirect Mail"
                    },
                   "field4":  {
                             "fieldname": "tax_year",
                             "fieldtype": "Int",
                             "label": "Tax Year"
                    },
                   "field5":  {
                              "fieldname": "tax_amount",
                              "fieldtype": "Currency",
                              "label": "Tax Amount"
                    },
                   "field6":  {
                             "fieldname": "payment_status",
                             "fieldtype": "Select",
                             "label": "Payment Status",
                              "options": "Paid\nUnpaid"
                    }
                 }
              },
               {
                "name": "Business Tax",
                "child_table": 0,
                "fields": {
                   "field1":  {
                             "fieldname": "tax_id",
                              "fieldtype": "Data",
                              "label": "Tax ID"
                     },
                    "field2":  {
                                "fieldname": "business_id",
                                "fieldtype": "Link",
                                "label": "Business ID",
                                "options": "Business Account"
                     },
                    "field3":  {
                              "fieldname": "tax_year",
                              "fieldtype": "Int",
                              "label": "Tax Year"
                    },
                   "field4":   {
                              "fieldname": "tax_amount",
                              "fieldtype": "Currency",
                               "label": "Tax Amount"
                   },
                 "field5":    {
                             "fieldname": "payment_status",
                             "fieldtype": "Select",
                             "label": "Payment Status",
                              "options": "Paid\nUnpaid"
                   }
                 }
              },
              {
                "name": "Food License",
                "child_table": 0,
                "fields": {
                  "field1": {
                            "fieldname": "license_id",
                            "fieldtype": "Data",
                            "label": "License ID"
                   },
                  "field2":  {
                            "fieldname": "business_id",
                             "fieldtype": "Link",
                             "label": "Business ID",
                             "options": "Business Account"
                   },
                  "field3":  {
                            "fieldname": "issue_date",
                            "fieldtype": "Date",
                            "label": "Issue Date"
                   },
                  "field4":  {
                            "fieldname": "expiry_date",
                             "fieldtype": "Date",
                            "label": "Expiry Date"
                    },
                  "field5":  {
                            "fieldname": "license_status",
                            "fieldtype": "Select",
                            "label": "License Status",
                             "options": "Active\nExpired\nSuspended"
                    },
                   "field6":  {
                             "fieldname": "license_type",
                             "fieldtype": "Select",
                             "label": "License Type",
                              "options": "Restaurant\nCatering\nFood Truck\nBakery\nOther"
                    }
                 }
              },
               {
                "name": "Marriage Registration",
                "child_table": 0,
                "fields": {
                  "field1":  {
                            "fieldname": "bride_name",
                            "fieldtype": "Data",
                            "label": "Bride's Name"
                    },
                   "field2":  {
                             "fieldname": "bride_age",
                             "fieldtype": "Int",
                             "label": "Bride's Age"
                   },
                  "field3":   {
                             "fieldname": "groom_name",
                             "fieldtype": "Data",
                             "label": "Groom's Name"
                   },
                  "field4":  {
                            "fieldname": "groom_age",
                            "fieldtype": "Int",
                            "label": "Groom's Age"
                  },
                 "field5":  {
                           "fieldname": "marriage_date",
                           "fieldtype": "Date",
                            "label": "Date of Marriage"
                 },
                "field6":  {
                          "fieldname": "marriage_place",
                          "fieldtype": "Data",
                           "label": "Place of Marriage"
                },
               "field7":  {
                         "fieldname": "witness1_name",
                         "fieldtype": "Data",
                         "label": "First Witness Name"
               },
              "field8":    {
                          "fieldname": "witness1_id",
                          "fieldtype": "Data",
                           "label": "First Witness ID Proof"
               },
               "field9":  {
                         "fieldname": "witness2_name",
                         "fieldtype": "Data",
                         "label": "Second Witness Name"
               },
              "field10":   {
                           "fieldname": "witness2_id",
                            "fieldtype": "Data",
                            "label": "Second Witness ID Proof"
                  }
                 }
              },
               {
                "name": "Marriage Certificate",
                "child_table": 0,
                "fields": {
                   "field1":  {
                              "fieldname": "certificate_id",
                               "fieldtype": "Data",
                              "label": "Certificate ID"
                    },
                   "field2":  {
                              "fieldname": "bride_name",
                              "fieldtype": "Data",
                              "label": "Bride's Name"
                   },
                  "field3":   {
                              "fieldname": "groom_name",
                              "fieldtype": "Data",
                              "label": "Groom's Name"
                   },
                  "field4":   {
                             "fieldname": "marriage_date",
                              "fieldtype": "Date",
                             "label": "Date of Marriage"
                   },
                  "field5":  {
                             "fieldname": "marriage_place",
                             "fieldtype": "Data",
                             "label": "Place of Marriage"
                  },
                 "field6":   {
                            "fieldname": "issuing_authority",
                            "fieldtype": "Data",
                            "label": "Issuing Authority"
                 },
                "field7":   {
                           "fieldname": "issue_date",
                           "fieldtype": "Date",
                           "label": "Issue Date"
                },
               "field8":   {
                           "fieldname": "expiry_date",
                           "fieldtype": "Date",
                           "label": "Expiry Date"
                   }
                 }
              },
              {
                "name": "Payment for Marriage Certificate",
                "child_table": 0,
                "fields": {
                    "field1":  {
                              "fieldname": "payment_id",
                              "fieldtype": "Data",
                              "label": "Payment ID"
                    },
                   "field2":   {
                               "fieldname": "certificate_id",
                               "fieldtype": "Data",
                               "label": "Marriage Certificate ID"
                   },
                  "field3":    {
                              "fieldname": "applicant_name",
                              "fieldtype": "Data",
                                "label": "Applicant Name"
                  },
                 "field4":   {
                            "fieldname": "payment_amount",
                            "fieldtype": "Currency",
                            "label": "Payment Amount"
                 },
                "field5":    {
                            "fieldname": "payment_date",
                            "fieldtype": "Date",
                            "label": "Payment Date"
                },
               "field6":    {
                            "fieldname": "payment_method",
                            "fieldtype": "Data",
                            "label": "Payment Method"
               },
              "field7":    {
                          "fieldname": "payment_status",
                          "fieldtype": "Select",
                           "label": "Payment Status",
                          "options":"Paid\nPending\nFailed"
                   }
                 }
              },
            
            
            
            
            
            
            
              
           
            
            
            
            
          
        ]

        for doctype in doctypes:
            # Check if the DocType already exists
            if frappe.db.exists("DocType", doctype["name"]):
                return f"DocType '{doctype['name']}' already exists!"
            else:
                # Create the custom DocType
                doc = frappe.get_doc({
                    "doctype": "DocType",
                    "module": "civic",
                    "name": doctype["name"],
                    "fields": [frappe._dict(field) for field in doctype["fields"].values()],
                    "permissions": [
                        {
                            "role": "System Manager",
                            "read": 1,
                            "write": 1,
                            "create": 1,
                            "delete": 1,
                            "submit": 0,
                            "cancel": 0,
                            "amend": 0
                        }
                    ],
                    "istable": doctype["child_table"]
                })
                doc.insert()
                frappe.db.commit()

        return "DocTypes created successfully!"

    except Exception as e:
        frappe.log_error(title="DocType Creation Error", message=str(e))
        return "Error occurred during DocType creation"

