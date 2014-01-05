<div class="row">
  <p><a class="btn" href="#/list"><span class="glyphicon glyphicon-backward"></span> Back to status page</a></p>
</div>
<div class="row" ng-cloak>
  <div class="col-md-4 col-md-push-8">
    <div class="panel panel-info">
      <div class="panel-heading">
        <h3 class="panel-title">Instructions</h3>
      </div>
      <div class="panel-body">
        <ol>
          <li>Choose a grade level.</li>
          <li>Choose a subject.</li>
          <li>The number of estimated allowed meetings will be shown to you. Plan your number of meetings according to that estimate.</li>
          <li>Enter one competency in each line and its corresponding number of meetings.</li>
          <li>To add another competency, click on the <code>Add</code> button or press the <code>Enter</code> key.</li>
          <li>To delete a competency, click on its corresponding <code>Remove</code> (<span class="glyphicon glyphicon-remove"></span>) button.</li>
          <li>Click <code>Save</code> when you're ready to save it.</li>
          <li>If it is saved successfully, a message box will appear telling you that it was saved successfully.</li>
          <li>Finally, you'll be redirected back to the status page where you should see the status of your subject and grade level updated.</li>
        </ol>
      </div>
    </div>
  </div>
  <div class="col-md-8 col-md-pull-4">
    <div class="panel panel-primary">
      <div class="panel-heading">
        <h3 class="panel-title">Edit Competencies</h3>
      </div>
      <div class="panel-body">
        <form name="frmCompetencies" class="form-horizontal" role="form">
          <div class="form-horizontal">
            <div class="form-group">
              <label for="inputSubject" class="col-xs-2 control-label">Subject:</label>
              <div class="col-xs-10">
                <select id="inputSubject" class="form-control" ng-model="subject" ng-options="choice for choice in subject_choices" required>
                  <option value="">Choose a subject</option>
                </select>
              </div>
            </div>
            <div class="form-group" ng-show="subject">
              <label for="inputGrade" class="col-xs-2 control-label">Grade:</label>
              <div class="col-xs-10">
                <select id="inputGrade" class="form-control" ng-model="grade" ng-options="n for n in get_grades_for_subject()" required>
                  <option value="">Choose a grade level</option>
                </select>
              </div>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-xs-12">
              <div class="alert alert-info" ng-show="get_max_meetings()">Please plan for <strong>{{get_max_meetings(subject,grade)}} meetings</strong> in the 3rd Quarter.
                Arrange them in chronological order.</div>
              <div class="alert alert-danger" ng-show="((get_total_meetings() > get_max_meetings()) && (get_total_meetings() > 1))">You have exceeed the maximum number of meetings allowed.
                Please recheck. </div>
            </div>
          </div>
          <div ng-show="get_max_meetings()">
            <table class="table table-responsive">
            <thead>
              <th class="col-xs-9">Competencies</th>
              <th class="col-xs-2">Meeting(s)</th>
              <th class="col-xs-1">Remove?</th>
            </thead>
            <tbody>
              <tr ng-repeat="item in competencies">
                <td>
                  <label class="sr-only" for="inputCompetency{{$index}}">{{item.competency}}</label>
                  <input type="text" class="form-control" id="inputCompetency{{$index}}" placeholder="Competency" ng-model="item.competency" required>
                </td>
                <td>
                  <label class="sr-only" for="inputDuration{{$index}}">Duration</label>
                  <input type="number" min="1" max="{{get_remaining_meetings(item.duration)}}" class="form-control" id="inputDuration{{$index}}" value="1" ng-model="item.duration" required>
                </td>
                <td>
                  <button type="button" class="btn btn-default" ng-click="delete_this_competency($index)">
                    <span class="glyphicon glyphicon-remove"></span>
                  </button>
                </td>
              </tr>
              <tr>
                <td>
                  <button class="btn btn-default" ng-click="add_new_competency()">Add</button>
                </td>
                <td colspan="2">
                  <span class="text-info">
                    <ng-pluralize count="get_total_meetings()" when="{'one': '1 meeting','other': '{} meetings'}"></ng-pluralize>
                  </span>
                </td>
              </tr>
            </tbody>
            </table>
            <div class="form-horizontal">
              <div class="form-group">
                <label class="col-xs-2 control-label">Teacher(s):</label>
                <div class="col-xs-10">
                  <!-- <p class="form-control-static">{{get_subject_teachers(subject, grade)}}</p> -->
                  <input class="form-control" id="disabledInput" type="text" placeholder="{{get_subject_teachers(subject, grade)}}" disabled>
                </div>
              </div>
              <div class="form-group">
                <label for="inputTeacher" class="col-xs-2 control-label">Created by:</label>
                <div class="col-xs-10">
                  <input type="text" class="form-control" ng-model="created_by" placeholder="Type your name" typeahead="name for name in teachers | filter:$viewValue | limitTo:8" required>
                </div>
              </div>
            </div>
            <hr>
            <button type="submit" class="btn btn-primary" ng-click="save_these_competencies()" ng-disabled="(!are_entries_valid())"><span class="glyphicon glyphicon-save"></span> Save</button>
            <button type="button" class="btn btn-danger" ng-click="delete_these_competencies()" ng-disabled="(!id)"><span class="glyphicon glyphicon-trash"></span> Delete</button>
            <!-- <button type="submit" class="btn btn-primary" data-toggle="modal" href="#saveModal">Save</button> -->
          </div>
        </form>
      </div>
    </div>
  </div>
</div>