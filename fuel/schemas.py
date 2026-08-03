from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import datetime, date, timedelta, time


class Course(BaseModel):
    id: int
    code: str
    code2: str
    title: str
    number_of_supervisors_winter: int
    number_of_supervisors_summer: int
    number_of_supervisors_september: int
    special_id: str
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    deleted_at: Optional[int] = None


class AssignmentEmail(BaseModel):
    id: int
    examperiod_id: int
    doctoral_id: int
    content: str
    title: str
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

class AssignmentPreference(BaseModel):
    id: int
    examperiod_id: int
    doctoral_id: int
    hours_remaining_tmp: int
    density: str
    density_day: int
    availabilities: str
    max_assignments: int
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None



class ExamDay(BaseModel):
    id: int
    examperiod_id: int
    day: datetime
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class ExamHour(BaseModel):
    id: int
    examperiod_id: int
    start: str
    end: str
    created_at: Optional[int] = None
    updated_at: Optional[int] = None

    @field_validator('start', 'end', mode='before')
    @classmethod
    def convert_time(cls, value):
        if isinstance(value, timedelta):
            total_seconds = int(value.total_seconds())
            hours, remainder = divmod(total_seconds, 3600)
            minutes, seconds = divmod(remainder, 60)
            return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        return str(value)


class ExamPeriod(BaseModel):
    id: int
    
    season: str = Field(max_length=32)
    academic_year: str
    
    # Поля с датами
    start: date
    end: date
    
    comment: str
    active: int
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None



class GlobalSetting(BaseModel):
    id: int
    linkexpirationdate: datetime
    
    alllinksopen: int
    emailhtml: int
    overridelinkexpirationdate: int
    
    emailencoding: str = Field(max_length=50)
    emailpriority: str = Field(max_length=50)
    
    emaildriver: str = Field(max_length=50)
    emailcharset: str = Field(max_length=20)
    emailfrom: str = Field(max_length=250)
    emailname: str = Field(max_length=250)
    emailreturn: str = Field(max_length=250)
    emailpathtosendmail: str = Field(max_length=250)
    emailsmtphost: str = Field(max_length=250)
    emailsmtpport: str = Field(max_length=20)
    emailsmtpusername: str = Field(max_length=250)
    emailsmtppassword: str = Field(max_length=250)
    emailsmtptimeout: str = Field(max_length=20)

    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class Migration(BaseModel):
    type: str = Field(max_length=25)
    name: str = Field(max_length=50)
    migration: str = Field(max_length=100)


class ProfessorCourse(BaseModel):
    id: int
    professor_id: int
    course_id: int
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class Professor(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    telephone: Optional[str] = None
    office: Optional[str] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    deleted_at: Optional[int] = None


class Upload(BaseModel):
    id: int
    friendly_name: str = Field(max_length=1024)
    file_name: str = Field(max_length=256)
    file_path: str = Field(max_length=1024)
    used: int
    uploaderId: int
    size: int
    created_at: Optional[int] = None
    updated_at: Optional[int] = None



class User(BaseModel):
    id: int
    
    username: str = Field(max_length=50)
    password: str = Field(max_length=255)
    email: str = Field(max_length=255)
    login_hash: str = Field(max_length=255)
    
    group: int
    last_login: int
    profile_fields: str
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class WelcomePost(BaseModel):
    id: int
    text: str 
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class Email(BaseModel):
    id: int
    examperiod_id: int
    subject: str
    html_content: str
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class EmailUrl(BaseModel):
    id: int
    token: str = Field(max_length=128)
    sent: int
    used: int
    
    doctoral_id: Optional[int] = None
    mail_id: Optional[int] = None
    valid_until: Optional[datetime] = None
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class Doctoral(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    am: Optional[str] = None
    registrationdate: Optional[str] = None
    telephone: Optional[str] = None
    comment: Optional[str] = None
    hours_remaining: int
    hours_completed: int
    graduated: int
    sendemail: int
    suspended: int
    max_assignments: int
    bonus_weight: float
    active: int
    created_at: Optional[int] = None
    updated_at: Optional[int] = None
    deleted_at: Optional[int] = None


class DoctoralSupervisor(BaseModel):
    professor_id: int
    doctoral_id: int


class ExamCourse(BaseModel):
    id: int
    examperiod_id: int
    examday_id: int
    examhour_id: int
    course_id: int
    assignments: Optional[str] = None
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None


class ExamSupervision(BaseModel):
    id: int
    doctoral_id: Optional[int] = None
    examcourse_id: Optional[int] = None
    hours: Optional[int] = None
    attended: int = 0
    comment: Optional[str] = None
    custom_exam_day: Optional[str] = None
    custom_exam_hour: Optional[str] = None
    
    created_at: Optional[int] = None
    updated_at: Optional[int] = None